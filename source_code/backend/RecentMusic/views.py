from Tool.checkDecorator import *
from .models import PlayHistoryList, PlayHistoryEntry


@method_checker('GET')
@user_checker(['user_id'])
def recent_played_songs(request):
    user_id = request.GET.get('user_id')
    user = User.objects.get(uid=user_id)
    resp = user.playhistorylist.history_detail()
    return JsonResponse({
        'code': '0',
        'msg': '成功',
        'data': resp
    })


@method_checker('POST')
@song_checker
@user_checker(['user_id'])
def record_play(request):
    song_id = request.POST.get('song_id')
    user_id = request.POST.get('user_id')
    play_history = PlayHistoryList.objects.get(user__uid=user_id)
    song = Song.objects.get(song_id=song_id)
    if play_history.content.filter(song=song):
        entry = play_history.content.get(song=song)
        play_history.content.remove(entry)
    entry = PlayHistoryEntry.objects.create(song=song)
    play_history.content.add(entry)
    return JsonResponse({
        'code': '0',
        'msg': '播放记录已添加'
    })

