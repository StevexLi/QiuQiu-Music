import ast

from django.db import models


class PlayHistoryList(models.Model):
    user = models.OneToOneField(to='User.User', to_field='uid', primary_key=True,
                                on_delete=models.CASCADE)
    content = models.ManyToManyField(to='RecentMusic.PlayHistoryEntry', default=None)

    def history_detail(self):
        resp = []
        recent_played_max = self.user.recent_played_max
        flag = 0
        for _ in self.content.all().order_by('-played_time'):
            resp.append(_.song.detail_info())
            flag += 1
            if flag >= recent_played_max:
                break
        return resp


class PlayHistoryEntry(models.Model):
    song = models.ForeignKey(to='Song.Song', to_field='song_id', on_delete=models.CASCADE)
    played_time = models.DateTimeField(auto_now_add=True)
