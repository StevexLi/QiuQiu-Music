from django.db.models import F

from SongList.models import likeList
from Tool.bucket import bucket
from Tool.checkDecorator import *
from Tool.fileHandler import upload_cover
from Tool.quickNotification import follower_notification, quick_notification


# Create your views here.
@method_checker('POST')
@user_checker(['user_id'])
@song_checker
@list_checker
def add_song_to_list(request):
    """
    add the song "song_id" to list "list_id". use POST. also use "user_id" to check permission.

    :param request:"song_id", "list_id" and "user_id" must be used
    :return: basic response
    """
    data = request.parsed_data
    song_id = data.get('song_id')
    list_id = data.get('list_id')
    user_id = data.get('user_id')
    song_list = SongList.objects.get(list_id=list_id)
    if song_list.creator_id != int(user_id):
        return JsonResponse({
            'code': '1006',
            'msg': '没有权限执行此操作'
        })
    if song_list.content.filter(song_id=song_id).exists():
        return JsonResponse({
            'code': '1007',
            'msg': '歌曲已在表中'
        })
    song = Song.objects.get(song_id=song_id)
    song_list.content.add(song)
    return JsonResponse({
        'code': '0',
        'msg': '成功添加歌曲进入歌单'
    })


@method_checker('POST')
@user_checker(['user_id'])
@null_checker(['title'])
def create_list(request):
    """
    :param request: must need "user_id", "title", others are optional
    :return: a list added to the user "user_id"
    """
    data = request.parsed_data
    user_id = data.get("user_id")
    title = data.get("title")
    tag1 = data.get('tag1', default='')
    tag2 = data.get('tag2', default='')
    tag3 = data.get('tag3', default='')
    tag4 = data.get('tag4', default='')
    tag5 = data.get('tag5', default='')
    tag6 = data.get('tag6', default='')
    if SongList.objects.filter(creator_id=user_id, title=title).exists():
        return JsonResponse({
            'code': '1009',
            'msg': '您已创建了此歌单，请勿创建重名歌单',
        })
    try:
        list = SongList.objects.create(title=title, tag1=tag1, tag2=tag2, tag3=tag3, tag4=tag4,
                                       tag5=tag5, tag6=tag6, creator_id=user_id)
        try:
            cover = request.FILES.get('cover')
            if cover is not None:
                upload_cover(cover, 'list_cover/', list.list_id)
                list.has_cover = True
                list.save()
        except Exception as e:
            print('create list err: ' + str(e))
            return JsonResponse({
                'code': '1005',
                'msg': '歌单已创建，但上传封面失败'
            })
        return JsonResponse({
            'code': '0',
            'msg': '创建歌单成功',
        })
    except Exception as e:
        print('create list err:' + str(e))
        return JsonResponse({
            'code': '1003',
            'msg': str(e)
        })


@method_checker('GET')
@list_checker
def get_list_info(request):
    """
    use 'list_id' to get the list's detailed info.
    This is an operation that doesn't need login.

    :param request: must use 'list_id'.
    :return: the detailed info of the list on success.
    """
    list_id = request.parsed_data.get('list_id')
    list = SongList.objects.get(list_id=list_id)
    info = list.detail_info()
    return JsonResponse({
        'code': '0',
        'msg': '查找歌单成功',
        'info': info,
    })


@method_checker('POST')
@user_checker(['operator_id'])
@list_checker
@song_checker
def remove_song_from_list(request):
    """
    remove song "song_id" from songlist "list_id", need "operator_id" to check permission.

    :param request: song_id, list_id and operator_id must be used.
    :return: basic response.
    """
    data = request.parsed_data
    operator_id = data.get('operator_id')
    list_id = data.get('list_id')
    song_id = data.get('song_id')
    if int(operator_id) != SongList.objects.get(list_id=list_id).creator_id:
        return JsonResponse({
            'code': '1006',
            'msg': '没有权限执行此操作'
        })
    list = SongList.objects.get(list_id=list_id)
    song = Song.objects.get(song_id=song_id)
    list.content.remove(song)
    return JsonResponse({
        'code': '0',
        'msg': '成功从歌单中删除歌曲'
    })


@method_checker('POST')
@user_checker(['operator_id'])
@list_checker
def update_list_info(request):
    """
    update the info of list "list_id", also need "operator_id" to check perm.
    other arguments are optional.

    :param request: must need "list_id" and "operator_id".
    :return: basic response.
    """

    data = request.parsed_data
    operator_id = data.get('operator_id')
    list_id = data.get('list_id')
    list = SongList.objects.get(list_id=list_id)
    if list.creator_id != int(operator_id):
        return JsonResponse({
            'code': '1005',
            'msg': '没有权限执行此操作'
        })
    list.title = data.get('title') if data.get('title') is not None else list.title
    list.tag1 = data.get('tag1') if data.get('tag1') is not None else list.tag1
    list.tag2 = data.get('tag2') if data.get('tag2') is not None else list.tag2
    list.tag3 = data.get('tag3') if data.get('tag3') is not None else list.tag3
    list.tag4 = data.get('tag4') if data.get('tag4') is not None else list.tag4
    list.tag5 = data.get('tag5') if data.get('tag5') is not None else list.tag5
    list.tag6 = data.get('tag6') if data.get('tag6') is not None else list.tag6
    list.introduction = data.get('introduction') if data.get('introduction') is not None else list.introduction
    list.save()
    try:
        cover = request.FILES.get('cover')
        if cover is not None:
            upload_cover(cover, 'list_cover/', list.list_id)
            if list.has_cover is False:
                list.has_cover = True
        list.save()
    except Exception as e:
        print('update song list err: ' + str(e))
        return JsonResponse({
            'code': '1006',
            'msg': '歌单信息更新成功，但封面上传失败'
        })
    return JsonResponse({
        'code': '0',
        'msg': '歌单信息更新成功'
    })


@method_checker('POST')
@user_checker(['operator_id'])
@list_checker
def delete_list(request):
    """
    must need "operator_id" and "list_id", also use "operator_id" to check perm.
    delete the list "list_id", only the owner or the admin have the perm to do so.

    :param request: must need "operator_id" and "list_id".
    :return: delete a songlist on success.
    """
    data = request.parsed_data
    list_id = data.get('list_id')
    operator_id = data.get('operator_id')
    user = User.objects.get(uid=operator_id)
    list = SongList.objects.get(list_id=list_id)
    creator_id = list.creator_id
    title = list.title
    if str(creator_id) != operator_id and not user.is_superuser:
        return JsonResponse({
            'code': '1005',
            'msg': '无权限执行此操作'
        })
    list.delete()
    if str(creator_id) == operator_id:
        return JsonResponse({
            'code': '0',
            'msg': '删除成功',
            'by_admin': '0',
        })
    else:
        msg_dict = {'user_id': user.uid, 'msg': '您的歌单《' + title + '》出现了一些问题，请核对一下再做上传吧'}
        quick_notification(msg_dict)
        return JsonResponse({
            'code': '0',
            'msg': '删除成功',
            'by_admin': '1',
        })


@method_checker('POST')
@user_checker(['user_id'])
@song_checker
def add_song_to_like(request):
    """
    add a song to the like list of user "user_id"

    :param request: "user_id" and "song_id"
    :return: basic response
    """
    data = request.parsed_data
    user_id = data.get('user_id')
    song_id = data.get('song_id')
    like_list = User.objects.get(uid=user_id).likelist
    song = Song.objects.get(song_id=song_id)
    if not like_list.content.contains(song):
        like_list.content.add(song)
        song.like = F('like') + 1
        song.save()
    else:
        return JsonResponse({
            'code': '1008',
            'msg': '此歌曲已添加入喜欢列表',
        })
    return JsonResponse({
        'code': '0',
        'msg': '添加进喜欢歌单成功'
    })


@method_checker('POST')
@user_checker(['user_id'])
@song_checker
def delete_song_from_like(request):
    """
    remove the song "song_id" from the like list of user "user_id"

    :param request: "song_id" and "user_id" are needed
    :return: basic response
    """
    data = request.parsed_data
    user_id = data.get('user_id')
    song_id = data.get('song_id')
    like_list = User.objects.get(uid=user_id).likelist
    song = Song.objects.get(song_id=song_id)
    if like_list.content.contains(song):
        like_list.content.remove(song)
        song.like = F('like') - 1
        song.save()
    return JsonResponse({
        'code': '0',
        'msg': '从喜欢歌单中删除成功'
    })


@method_checker('GET')
@user_checker(['user_id'])
def get_like_list(request):
    """
    get the like list of the user "user_id".

    :param request: "user_id" is the only needed
    :return: the content and the cover of like list
    """
    user_id = request.parsed_data.get('user_id')
    like_list = User.objects.get(uid=user_id).likelist
    info = like_list.detail_info()
    return JsonResponse({
        'code': '0',
        'msg': '查询用户喜欢歌单成功',
        'data': info,
    })


@method_checker('GET')
@user_checker(['user_id'])
@song_checker
def check_song_in_like_list(request):
    """
    check if the song "song_id" is in the like list of user "user_id"

    :param request: must use "song_id" and "user_id"
    :return: basic response, use "result" to mark the result
    """
    data = request.parsed_data
    song_id = data.get('song_id')
    user_id = data.get('user_id')
    like_list = User.objects.get(uid=user_id).likelist
    song = Song.objects.get(song_id=song_id)
    res = like_list.content.contains(song)
    return JsonResponse({
        'code': '0',
        'msg': '查询成功',
        'result': str(res)
    })


@method_checker('POST')
@user_checker(['operator_id'])
@list_checker
def share_song_list(request):
    """
    use this view function to switch the share status of the list "list_id"

    :param request: need "operator_id" and "list_id"
    :return: basic response, switch the share status of the list
    """
    data = request.parsed_data
    operator_id = data.get('operator_id')
    list_id = data.get('list_id')
    list = SongList.objects.get(list_id=list_id)
    if str(list.creator_id) != operator_id:
        return JsonResponse({
            'code': '1005',
            'msg': '无权限进行此操作'
        })
    list.sharable = not list.sharable
    if list.sharable is True:
        follower_notification(user_id=operator_id, share_type='歌单')
    list.save()
    return JsonResponse({
        'code': '0',
        'msg': '分享状态更改成功',
    })


def complain_song_list(request):
    if request.method != 'POST':
        data = request.POST
        creator_id = data.get('creator_id')
        list_id = data.get('list_id')
        if creator_id is None:
            return JsonResponse({
                'code': '1002',
                'msg': '未传入必需参数'
            })
        if not User.objects.filter(uid=creator_id).exists():
            return JsonResponse({
                'code': '1003',
                'msg': '不存在此用户'
            })
        if list_id is None:
            list = likeList.objects.get(creator_id=creator_id)
        else:
            list = SongList.objects.get(list_id=list_id)
        for song in list.content:
            key_name = '/song/' + song.song_id + '.mp3'
            bucket.audio_audit_submit(key_name, song.song_id)
        return JsonResponse({
            'code': '0',
            'msg': '投诉成功，歌单内所有歌曲已重新审核'
        })
    else:
        return JsonResponse({
            'code': '1001',
            'msg': '请求方式错误，请用POST'
        })
