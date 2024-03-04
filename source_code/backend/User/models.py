from django.contrib.auth.models import AbstractUser
from django.db import models

from SongList.models import SongList, likeList
from Tool.bucket import bucket
from properties import SONG_COVER_PREFIX, USER_DEFAULT_ICON


# Create your models here.
class User(AbstractUser):
    # 基本用户设置
    uid = models.BigAutoField('uid', primary_key=True, auto_created=True)
    has_icon = models.BooleanField('has_icon', default=False)
    introduction = models.CharField('introduction', max_length=200, default='这个用户很神秘，还没有写任何介绍。')
    recent_played_max = models.PositiveIntegerField('recent_played_max_number', default=50)

    def detail_info(self):
        info = {
            'uid': self.uid,
            'username': self.username,
            'introduction': self.introduction,
            'has_icon': self.has_icon,
            'icon_address': self.get_icon_address(),
            'is_admin': self.is_staff,
            'recent_played_max': self.recent_played_max,
        }
        return info

    def get_icon_address(self):
        if self.has_icon:
            prefix = 'user/' + str(self.uid)
            prefix = bucket.list_file(prefix)
            icon_address = SONG_COVER_PREFIX + prefix
        else:
            icon_address = USER_DEFAULT_ICON
        return icon_address

    def __str__(self):
        return self.username
