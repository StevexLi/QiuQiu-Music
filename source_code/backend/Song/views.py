import os.path
import uuid

from django.db.models import F

from Tool.bucket import bucket
from Tool.checkDecorator import *
from Tool.fileHandler import save_file
from Tool.quickNotification import follower_notification, quick_notification


# Create your views here.
@method_checker('POST')
@user_checker(['uploader_id'])
@null_checker(['title'])
def upload_song(request):
    """
    use POST, "uploader_id", "title", "local_file" are needed.

    :param request: "uploader_id", "title", "local_file" are must be used.
    :return: storage the song in cloud.
    """
    data = request.parsed_data
    title = data.get('title')
    singer = data.get('singer') if data.get('singer') is not None else 'Various Artists'
    introduction = data.get('introduction') if data.get('introduction') is not None else ''
    tag1 = data.get('tag1') if data.get('tag1') is not None else ''
    tag2 = data.get('tag2') if data.get('tag2') is not None else ''
    tag3 = data.get('tag3') if data.get('tag3') is not None else ''
    tag4 = data.get('tag4') if data.get('tag4') is not None else ''
    tag5 = data.get('tag5') if data.get('tag5') is not None else ''
    tag6 = data.get('tag6') if data.get('tag6') is not None else ''
    cover = request.FILES.get('cover')
    lyric = request.FILES.get('lyric')
    local_file = request.FILES.get('local_file')
    if local_file is None:
        return JsonResponse({
            'code': '1003',
            'msg': 'local_file 不可以为空'
        })
    uploader_id = data.get('uploader_id')
    try:
        new_song = Song.objects.create(title=title, singer=singer, introduction=introduction,
                                       uploader_id=uploader_id, tag1=tag1, tag2=tag2, tag3=tag3, tag4=tag4,
                                       tag5=tag5, tag6=tag6)
        # upload song file
        suffix = os.path.splitext(local_file.name)[-1]
        key_name = 'song/' + str(new_song.song_id) + suffix
        temp_uuid = uuid.uuid1()
        local_file_path = save_file(local_file, temp_uuid, suffix)
        bucket.upload_file(local_file_path, key_name)
        os.remove(local_file_path)
        # upload cover file
        if cover is not None:
            suffix = os.path.splitext(cover.name)[-1]
            key_name = 'cover/' + str(new_song.song_id) + suffix
            cover_path = save_file(cover, temp_uuid, suffix)
            bucket.upload_file(cover_path, key_name)
            os.remove(cover_path)
            new_song.has_cover = True
        # upload lyric file
        if lyric is not None:
            key_name = 'lyric/' + str(new_song.song_id) + '.lrc'
            lyric_path = save_file(lyric, temp_uuid, '.lrc')
            bucket.upload_file(lyric_path, key_name)
            os.remove(lyric_path)
            new_song.has_lyric = True
        new_song.save()
        follower_notification(user_id=uploader_id, share_type='歌曲')
        return JsonResponse({
            'code': '0',
            'msg': '上传歌曲成功'
        })
    except Exception as e:
        print('上传歌曲失败：' + str(e))
        return JsonResponse({
            'code': '1005',
            'msg': '上传歌曲失败'
        })


def update_song(request):
    """
    update a song's information, only the creator of the song can do this.

    :param request: operator_id and song_id must be used. others are optional.
    :return: msg and code, in Json.
    """
    if request.method == 'POST':
        data = request.POST
        operator_id = data.get('operator_id')
        song_id = data.get('song_id')
        if song_id is None:
            return JsonResponse({
                'code': '1002',
                'msg': '必需参数未传入'
            })
        if not Song.objects.filter(song_id=song_id).exists():
            return JsonResponse({
                'code': '1003',
                'msg': '此歌曲不存在'
            })
        song = Song.objects.get(song_id=song_id)
        if str(song.uploader_id) != operator_id:
            return JsonResponse({
                'code': '1005',
                'msg': '无权限执行此操作'
            })
        song.title = data.get('title') if data.get('title') is not None else song.title
        song.singer = data.get('singer') if data.get('singer') is not None else song.singer
        song.introduction = data.get('introduction') if data.get('introduction') is not None else song.introduction
        song.tag1 = data.get('tag1') if data.get('tag1') is not None else song.tag1
        song.tag2 = data.get('tag2') if data.get('tag2') is not None else song.tag2
        song.tag3 = data.get('tag3') if data.get('tag3') is not None else song.tag3
        song.tag4 = data.get('tag4') if data.get('tag4') is not None else song.tag4
        song.tag5 = data.get('tag5') if data.get('tag5') is not None else song.tag5
        song.tag6 = data.get('tag6') if data.get('tag6') is not None else song.tag6
        try:
            temp_uuid = uuid.uuid1()
            # update song
            local_file = request.FILES.get('local_file')
            if local_file is not None:
                prefix = 'song/' + str(song.song_id)
                key_name = bucket.list_file(prefix)
                bucket.delete_file(key_name)
                suffix = os.path.splitext(local_file.name)[-1]
                key_name = 'song/' + str(song.song_id) + suffix
                local_file_path = save_file(local_file, temp_uuid, suffix)
                bucket.upload_file(local_file_path, key_name)
                os.remove(local_file_path)
            # update cover
            cover = request.FILES.get('cover')
            if cover is not None:
                prefix = 'cover/' + str(song.song_id)
                key_name = bucket.list_file(prefix)
                if key_name != 'err':
                    bucket.delete_file(key_name)
                suffix = os.path.splitext(cover.name)[-1]
                key_name = 'cover/' + str(song.song_id) + suffix
                cover_path = save_file(cover, temp_uuid, suffix)
                bucket.upload_file(cover_path, key_name)
                os.remove(cover_path)
                if song.has_cover is False:
                    song.has_cover = True
            # update lyric
            lyric = request.FILES.get('lyric')
            if lyric is not None:
                prefix = 'lyric/' + str(song_id)
                key_name = bucket.list_file(prefix)
                if key_name != 'err':
                    bucket.delete_file(key_name)
                key_name = 'lyric/' + str(song.song_id) + '.lrc'
                lyric_path = save_file(lyric, temp_uuid, '.lrc')
                bucket.upload_file(lyric_path, key_name)
                os.remove(lyric_path)
                if song.has_lyric is False:
                    song.has_lyric = True
            song.save()
        except Exception as e:
            print('update failed: ' + str(e))
            return JsonResponse({
                'code': '1004',
                'msg': '更新歌曲信息失败',
            })
        return JsonResponse({
            'code': '0',
            'msg': '更新歌曲信息成功'
        })
    else:
        return JsonResponse({
            'code': '1001',
            'msg': '请求方法错误，请用POST',
        })


@method_checker('GET')
@song_checker
def get_song_info(request):
    """
    :param: request: "song_id" is the only thing needed. use GET.
    :return: the info of the song, the address is the way to load the song.
    """
    song_id = request.parsed_data.get("song_id")
    song = Song.objects.get(song_id=song_id)
    song_info = song.detail_info()
    res = {
        'code': '0',
        'msg': '查找成功',
        'info': song_info,
    }
    return JsonResponse(res)


def delete_song(request):
    """
    delete the song "song_id", need "operator_id" to judge permission.

    :param request: need "song_id" and "operator_id"
    :return: basic response, delete a song "song_id"
    """
    if request.method == 'POST':
        song_id = request.POST.get('song_id')
        operator_id = request.POST.get('operator_id')
        if song_id is None:
            return JsonResponse({
                'code': '1002',
                'msg': '未传入必需参数'
            })
        if not User.objects.filter(uid=operator_id).exists():
            return JsonResponse({
                'code': '1003',
                'msg': '不存在此用户'
            })
        if not Song.objects.filter(song_id=song_id).exists():
            return JsonResponse({
                'code': '1004',
                'msg': '不存在此歌曲'
            })
        user = User.objects.get(uid=operator_id)
        song = Song.objects.get(song_id=song_id)
        title = song.title
        uploader_id = song.uploader_id
        if str(song.uploader_id) != operator_id and not user.is_superuser:
            return JsonResponse({
                'code': '1005',
                'msg': '无权限执行此操作'
            })
        try:
            prefix = 'song/' + str(song_id)
            key_name = bucket.list_file(prefix)
            bucket.delete_file(key_name)
            prefix = 'cover/' + str(song_id)
            key_name = bucket.list_file(prefix)
            if key_name != 'err':
                bucket.delete_file(key_name)
            prefix = 'lyric/' + str(song_id)
            key_name = bucket.list_file(prefix)
            if key_name != 'err':
                bucket.delete_file(key_name)
            song.delete()
            if str(song.uploader_id) == operator_id:
                return JsonResponse({
                    'code': '0',
                    'msg': '删除成功',
                    'byAdmin': '0',
                })
            else:
                msg_dict = {'user_id': uploader_id, 'msg': '您的歌曲《' + title + '》出现了一些问题，请核对一下再做上传吧'}
                quick_notification(msg_dict)
                return JsonResponse({
                    'code': '0',
                    'msg': '删除成功',
                    'byAdmin': '1',
                })
        except Exception as e:
            print('delete err: ' + str(e))
            return JsonResponse({
                'code': '1006',
                'msg': str(e)
            })
    else:
        return JsonResponse({
            'code': '1001',
            'msg': '请求方法错误，请使用POST'
        })


@method_checker('POST')
@song_checker
def increase_played(request):
    """
    increase the "played" on song "song_id" by 1 every time this view is called.
    need "song_id".

    :param request: only need "song_id"
    :return: basic response
    """
    song_id = request.parsed_data.get('song_id')
    song = Song.objects.get(song_id=song_id)
    song.played = F('played') + 1
    song.save()
    return JsonResponse({
        'code': '0',
        'msg': '播放量增加成功'
    })
