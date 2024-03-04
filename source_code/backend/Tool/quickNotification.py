from Notifications.models import Notification
from User.models import User


def quick_notification(message_dict):
    user_id = message_dict['user_id']
    msg = message_dict['msg']
    Notification.objects.create(user_id=user_id, message=msg)


def follower_notification(user_id, share_type):
    user = User.objects.get(uid=user_id)
    follower_list = list(user.describers.all())
    for _ in follower_list:
        msg = '您关注的用户' + user.username + '分享了新的' + share_type + '哦！快去围观一下吧！'
        msg_dict = {'user_id': _.creator_id, 'msg': msg}
        quick_notification(msg_dict)


