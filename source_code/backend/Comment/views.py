from Tool.checkDecorator import *
from .models import Comment


@method_checker('POST')
@user_checker(['user_id'])
@song_checker
@null_checker(['content'])
def add_comment(request):
    data = request.POST
    song_id = data.get('song_id')
    content = data.get('content')
    user_id = data.get('user_id')
    song = Song.objects.get(song_id=song_id)
    user = User.objects.get(uid=user_id)
    comment = Comment(user=user, song=song, content=content)
    comment.save()

    return JsonResponse({
        'code': '0',
        'msg': '评论添加成功',
    })


@method_checker('GET')
@song_checker
def get_comment_info(request):
    song_id = request.GET.get('song_id')
    song = Song.objects.get(song_id=song_id)
    comments = Comment.objects.filter(song=song).order_by('-created_at')

    comment_info = []
    for comment in comments:
        comment_info.append({
            'comment_id': comment.id,
            'user': comment.user.detail_info(),
            'content': comment.content,
            'created_at': comment.created_at
        })

    return JsonResponse({
        'code': '0',
        'msg': '获取评论信息成功',
        'data': comment_info
    })


@method_checker('POST')
@user_checker(['operator_id'])
@null_checker(['comment_id'])
def delete_comment(request):
    comment_id = request.POST.get('comment_id')
    operator_id = request.POST.get('operator_id')

    try:
        comment = Comment.objects.get(id=comment_id)
        if not comment_id.isdigit():
            return JsonResponse({
                'code': '1009',
                'msg': 'comment_id不是数字'
            })

        if comment.user.uid != int(operator_id):
            return JsonResponse({
                'code': '1005',
                'msg': '无权限删除该评论'
            })

        comment.delete()

        return JsonResponse({
            'code': '0',
            'msg': '评论删除成功'
        })
    except Comment.DoesNotExist:
        return JsonResponse({
            'code': '1006',
            'msg': '评论不存在'
        })
