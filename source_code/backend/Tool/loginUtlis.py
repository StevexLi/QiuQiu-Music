import jwt
import time

from django.http import JsonResponse

from User.models import User
from properties import TOKEN_KEY


def sign_token(payload, exp=3600 * 24 * 14):
    payload['exp'] = time.time() + exp
    token = jwt.encode(payload, TOKEN_KEY, 'HS256')
    return token


def logging_check(func):
    def wrap(request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return JsonResponse({
                'code': '403',
                'msg': '请登录'
            })
        try:
            res = jwt.decode(token, TOKEN_KEY, algorithms='HS256')
        except Exception as e:
            print('jwt decode error is %s' % e)
            result = {'code': '403', 'error': 'please login'}
            return JsonResponse(result)
        username = res['username']
        if not User.objects.filter(username=username).exists():
            return JsonResponse({
                'code': '403',
                'msg': '用户不存在'
            })
        request.POST.operator_id = User.objects.get(username=username).uid
        print(request.POST.operator_id)
        return func(request, *args, **kwargs)

    return wrap
