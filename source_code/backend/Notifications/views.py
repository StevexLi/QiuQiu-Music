from Tool.checkDecorator import *
from .models import Notification


@method_checker('POST')
@user_checker(['user_id'])
def create_notification(request):
    user_id = request.POST.get('user_id')
    message = request.POST.get('message')
    if not message:
        return JsonResponse({
            'code': '1002',
            'msg': '不能传入空message'
        })
    user = User.objects.get(uid=user_id)
    notification = Notification(user=user, message=message)
    notification.save()
    return JsonResponse({
        'code': '0',
        'msg': '通知创建成功'
    })


@method_checker('GET')
@user_checker(['user_id'])
def get_notifications(request):
    user_id = request.GET.get('user_id')
    user = User.objects.get(uid=user_id)
    notifications = Notification.objects.filter(user=user).order_by('-created_at')
    notification_info = []
    count = 0
    while count < min(len(notifications), 30):
        notification = notifications[count]
        notification_info.append({
            'id': notification.id,
            'message': notification.message,
            'created_at': notification.created_at
        })
        count += 1
    return JsonResponse({
        'code': '0',
        'msg': '获取通知成功',
        'data': notification_info
    })