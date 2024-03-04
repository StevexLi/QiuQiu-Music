import re

from DescribeList.models import DescribeList
from RecentMusic.models import PlayHistoryList
from SongList.models import likeList
from Tool.checkDecorator import *
from Tool.loginUtlis import sign_token, logging_check
from Tool.pageTool import page_result
from Tool.fileHandler import upload_cover


# Create your views here.
@method_checker('POST')
@null_checker(['username', 'password_1', 'password_2'])
def register(request):
    """
    :param: request:use "data", need 'username', 'password_1', 'password_2'
    :return: JsonResponse, on Success storage user with 'username' and 'password_1', 'password_2' is a checker.
    """
    # TODO 需要给这里写一个md5加密存储
    data = request.parsed_data
    username = data.get("username")
    password = data.get("password_1")
    password_2 = data.get("password_2")
    if password_2 != password:
        return JsonResponse({
            'code': '1001',
            'msg': '两次输入密码不一致'
        })
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            'code': '1006',
            'msg': '用户名已存在',
        })
    if re.fullmatch("[A-Za-z0-9_]{8,30}", password) is None:
        return JsonResponse({
            'code': '1003',
            'msg': '密码不符合规范',
        })
    if re.fullmatch("[A-Za-z0-9_\u4e00-\u9fa5\u0800-\u4e00]{3,30}", username) is None:
        return JsonResponse({
            'code': '1004',
            'msg': '用户名不符合规范',
        })
    new_user = User.objects.create(username=username, password=password)
    init_user(new_user)
    return JsonResponse({
        'code': '0',
        'msg': '注册成功',
    })


@method_checker('POST')
@null_checker(['username', 'password'])
def login(request):
    """
    :param request: need 'username' and 'password'
    :return: on success, return token. During other operation, please take the token with request.
    """
    data = request.parsed_data
    username = data.get('username')
    password = data.get('password')
    if not User.objects.filter(username=username).exists():
        return JsonResponse({
            'code': '1003',
            'msg': '此用户不存在',
        })
    user = User.objects.get(username=username)
    if user.password != password:
        return JsonResponse({
            'code': '1001',
            'msg': '密码不正确',
        })
    payload = {'username': user.username}
    token = sign_token(payload)
    return JsonResponse({
        'code': '0',
        'msg': "登录成功",
        'token': token,
        'uid': user.uid,
    })


@method_checker('GET')
@user_checker(['operator_id'])
def get_song_list_all(request):
    """
    get all the song list of the user "operator_id", use "page_num" to mark the get result on certain page

    :param request: need "operator_id" and "page_num"
    :return: all the info of list of "operator_id" in "page_num"
    """
    data = request.parsed_data
    operator_id = data.get('operator_id')
    user = User.objects.get(uid=operator_id)
    list_set = list(user.songlist_set.all())
    list_set.reverse()
    resp = []
    for _ in list_set:
        resp.append(_.detail_info())
    return JsonResponse({
        'code': '0',
        'msg': '查询此用户歌单成功',
        'data': resp,
        'total': len(resp),
    })


@method_checker('GET')
@user_checker(['user_id'])
def get_list_sharable(request):
    """
    return the sharable lists of the user "user_id", use "page_num" to mark the get result on certain page

    :param request: need "user_id" and "page_num"
    :return: sharable song lists
    """
    data = request.parsed_data
    user_id = data.get('user_id')
    user = User.objects.get(uid=user_id)
    list_set = list(user.songlist_set.filter(sharable=True).all())
    list_set.reverse()
    resp = []
    for _ in list_set:
        resp.append(_.detail_info())
    return JsonResponse({
        'code': '0',
        'msg': '查询此用户歌单成功',
        'data': resp,
        'total': len(resp),
    })


@method_checker('GET')
@user_checker(['user_id'])
def get_uploaded_song(request):
    data = request.parsed_data
    user_id = data.get('user_id')
    user = User.objects.get(uid=user_id)
    song_set = list(user.song_set.all())
    song_set.reverse()
    resp = []
    for _ in song_set:
        resp.append(_.detail_info())
    return JsonResponse({
        'code': '0',
        'msg': '查询歌曲成功',
        'data': resp
    })


@method_checker('GET')
@user_checker(['user_id'])
def get_basic_info(request):
    data = request.parsed_data
    user_id = data.get('user_id')
    user = User.objects.get(uid=user_id)
    info = user.detail_info()
    return JsonResponse({
        'code': '0',
        'msg': '查找成功',
        'data': info
    })


@method_checker('POST')
@user_checker(['user_id'])
def update_basic_info(request):
    data = request.parsed_data
    user_id = data.get('user_id')
    user = User.objects.get(uid=user_id)
    user.username = data.get('username', '') if data.get('username', '') != '' else user.username
    user.introduction = data.get('introduction', '') if data.get('introduction', '') != '' else user.introduction
    user.recent_played_max = data.get('recent_played_max', '') if data.get('recent_played_max',
                                                                           '') != '' else user.recent_played_max
    icon = request.FILES.get('icon')
    try:
        if icon is not None:
            upload_cover(icon, 'user/', user_id)
            user.has_icon = True
    except Exception as e:
        print('update basic info err:' + str(e))
        user.save()
        return JsonResponse({
            'code': '1008',
            'msg': '用户信息更新完成，但上传头像失败'
        })
    user.save()
    return JsonResponse({
        'code': '0',
        'msg': '更改用户基本信息成功',
    })


def init_user(new_user):
    likeList.objects.create(creator=new_user)
    DescribeList.objects.create(creator=new_user)
    PlayHistoryList.objects.create(user=new_user)


@logging_check
def login_test(request):
    print('login success!')
    return JsonResponse({
        'code': '0',
        'msg': 'success',
    })
