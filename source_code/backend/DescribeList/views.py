from Tool.checkDecorator import *


# Create your views here.
@method_checker('POST')
@user_checker(['user_id', 'describer_id'])
def add_to_describe_list(request):
    data = request.POST
    user_id = data['user_id']
    describer_id = data['describer_id']
    if user_id == describer_id:
        return JsonResponse({
            'code': '1008',
            'msg': '一个用户不可以关注他自己',
        })
    user = User.objects.get(uid=user_id)
    describer = User.objects.get(uid=describer_id)
    if user.describelist.content.contains(describer):
        return JsonResponse({
            'code': '1009',
            'msg': '已经关注此用户了',
        })
    user.describelist.content.add(describer)
    return JsonResponse({
        'code': '0',
        'msg': '成功加入关注列表',
    })


@method_checker('POST')
@user_checker(['user_id', 'describer_id'])
def remove_from_describe_list(request):
    data = request.POST
    user_id = data['user_id']
    describer_id = data['describer_id']
    user = User.objects.get(uid=user_id)
    describer = User.objects.get(uid=describer_id)
    user.describelist.content.remove(describer)
    return JsonResponse({
        'code': '0',
        'msg': '成功移除出关注列表',
    })


@method_checker('GET')
@user_checker(['user_id'])
def get_describer_list(request):
    data = request.GET
    user_id = data['user_id']
    content = list(User.objects.get(uid=user_id).describelist.content.all())
    resp = []
    for _ in content:
        resp.append(_.detail_info())
    return JsonResponse({
        'code': '0',
        'msg': '查找关注列表成功',
        'data': resp
    })


@method_checker('GET')
@user_checker(['user_id', 'describer_id'])
def check_describer_in_user_list(request):
    data = request.GET
    user_id = data['user_id']
    describer_id = data['describer_id']
    user = User.objects.get(uid=user_id)
    describer = User.objects.get(uid=describer_id)
    resp = user.describelist.content.contains(describer)
    return JsonResponse({
        'code': '0',
        'msg': '查找成功',
        'status': resp,
    })


