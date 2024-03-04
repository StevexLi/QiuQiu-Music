from Complain.models import Complain
from Tool.checkDecorator import *
from Tool.quickNotification import quick_notification


# Create your views here.
@method_checker('GET')
def get_complain(request):
    res = Complain.objects.all()
    resp = []
    for _ in res:
        resp.append(_.detail_info())
    return JsonResponse({
        'code': '0',
        'msg': '查找完成',
        'data': resp,
    })


@method_checker('POST')
@user_checker(['user_id'])
@null_checker(['obj_id', 'type', 'content'])
@obj_checker
def create_complain(request):
    data = request.parsed_data
    user_id = data.get('user_id')
    obj_id = data.get('obj_id')
    c_type = eval(data.get('type'))
    content = data.get('content')
    Complain.objects.create(complainer_id=user_id, type=c_type, obj_id=obj_id, content=content)
    return JsonResponse({
        'code': '0',
        'msg': '投诉成功',
    })


@method_checker('POST')
@null_checker(['result', 'complain_id'])
def execute_complain(request):
    data = request.parsed_data
    result = eval(data.get('result'))
    complain_id = data.get('complain_id')
    complain = Complain.objects.get(id=complain_id)
    complainer_id = complain.complainer_id
    extra_msg = data.get('extra_msg')
    complainee_id = complain.get_uploader_id()
    if result:
        msg = '您针对《' + complain.get_obj().title + '》的投诉已经成功受理！'
        msg_dict_1 = {
            'user_id': complainer_id,
            'msg': msg,
        }
        quick_notification(msg_dict_1)
        msg = '您上传的作品《' + complain.get_obj().title + '》出了一点小问题，现暂时下架。'
        if extra_msg is not None or extra_msg != '':
            msg += '原因是：' + extra_msg
        msg_dict_2 = {
            'user_id': complainee_id,
            'msg': msg,
        }
        quick_notification(msg_dict_2)
        complain.obj_delete()
    else:
        msg = '您针对《' + complain.get_obj().title + '》的投诉未成功受理！'
        if extra_msg is not None or extra_msg != '':
            msg += '原因是：' + extra_msg
        msg_dict = {
            'user_id': complainer_id,
            'msg': msg,
        }
        quick_notification(msg_dict)
    complain.delete()
    return JsonResponse({
        'code': '0',
        'msg': '投诉处理完成'
    })



