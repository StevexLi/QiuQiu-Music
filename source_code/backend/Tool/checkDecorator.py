import os

from django.http import JsonResponse
from requests import Response

from User.models import User
from Song.models import Song
from SongList.models import SongList


def method_checker(method):
    def decorator(func):
        def wrap(request, *args, **kwargs):
            if request.method != method:
                msg = '请求方式错误， 请使用' + method + '方法'
                return JsonResponse({
                    'code': '1001',
                    'msg': msg,
                })
            else:
                if method == 'GET':
                    request.parsed_data = request.GET.copy()
                else:
                    request.parsed_data = request.POST.copy()
                return func(request, *args, **kwargs)

        return wrap

    return decorator


def user_checker(user_params):
    def decorator(func):
        def wrap(request, *args, **kwargs):
            params = {}
            for _ in user_params:
                item = request.parsed_data.get(_, None)
                if item is None or item == '':
                    msg = '有参数未传入，' + _ + '是空'
                    return JsonResponse({
                        'code': '1002',
                        'msg': msg,
                    })
                params[_] = item
            try:
                for (key, value) in params.items():
                    value = int(value)
                    if not User.objects.filter(uid=value).exists():
                        msg = key + '对应的用户不存在'
                        return JsonResponse({
                            'code': '1003',
                            'msg': msg,
                        })
            except ValueError as e:
                print('user_checker err: ' + str(e))
                return JsonResponse({
                    'code': '1004',
                    'msg': '有传入的参数不是整数',
                })
            return func(request, *args, **kwargs)

        return wrap

    return decorator


def song_checker(func):
    def wrap(request, *args, **kwargs):
        song_id = request.parsed_data.get('song_id', None)
        if song_id is None or song_id == '':
            return JsonResponse({
                'code': '1002',
                'msg': '有参数未传入，song_id是空'
            })
        try:
            song_id = int(song_id)
            if not Song.objects.filter(song_id=song_id).exists():
                return JsonResponse({
                    'code': '1005',
                    'msg': '对应的歌曲不存在'
                })
        except ValueError:
            return JsonResponse({
                'code': '1004',
                'msg': '有传入的参数不是整数',
            })
        return func(request, *args, **kwargs)

    return wrap


def list_checker(func):
    def wrap(request, *args, **kwargs):
        list_id = request.parsed_data.get('list_id', None)
        if list_id is None or list_id == '':
            return JsonResponse({
                'code': '1002',
                'msg': '有参数未传入，list_id是空'
            })
        try:
            list_id = int(list_id)
            if not SongList.objects.filter(list_id=list_id).exists():
                return JsonResponse({
                    'code': '1006',
                    'msg': '对应的歌单不存在'
                })
        except ValueError:
            return JsonResponse({
                'code': '1004',
                'msg': '有传入的参数不是整数',
            })
        return func(request, *args, **kwargs)

    return wrap


def null_checker(params):
    def decorator(func):
        def wrap(request, *args, **kwargs):
            try:
                for _ in params:
                    judge = request.parsed_data.get(_, None)
                    if judge is None or judge == '':
                        return JsonResponse({
                            'code': '1002',
                            'msg': '有参数未传入，' + _ + '是空',
                        })
                return func(request, *args, **kwargs)
            except Exception as e:
                print(e)
        return wrap

    return decorator


def page_num_checker(func):
    def wrap(request, *args, **kwargs):
        page_num = request.parsed_data.get('page_num', None)
        if page_num is None or page_num == '':
            request.parsed_data['page_num'] = '1'
            page_num = request.parsed_data.get('page_num', None)
        if not page_num.isdigit():
            return JsonResponse({
                'code': '1006',
                'msg': '传入的页数不是整数',
            })
        return func(request, *args, **kwargs)

    return wrap


def obj_checker(func):
    def wrap(request, *args, **kwargs):
        if eval(request.parsed_data.get('type')):
            request.parsed_data['song_id'] = request.parsed_data.get('obj_id')
            checker = song_checker(func)
            return checker(request, *args, **kwargs)
        else:
            request.parsed_data['list_id'] = request.parsed_data.get('obj_id')
            checker = list_checker(func)
            return checker(request, *args, **kwargs)
    return wrap


