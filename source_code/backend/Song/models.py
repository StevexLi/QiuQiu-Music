from django.core.validators import MinValueValidator
from django.db import models

from Tool.bucket import bucket
from properties import SONG_DEFAULT_COVER, SONG_COVER_PREFIX, SONG_LYRIC_PREFIX, SONG_ADDRESS_PREFIX
from Tool.encode import get_code


# Create your models here.
class Song(models.Model):
    # 歌曲基本信息
    song_id = models.BigAutoField('song_id', primary_key=True, auto_created=True)
    title = models.CharField('Title', max_length=50)
    singer = models.CharField('Singer', max_length=30, default='Various Artists')
    introduction = models.CharField('Introduction', max_length=300, default='')
    uploader = models.ForeignKey(to="User.User", to_field='uid', on_delete=models.DO_NOTHING)
    like = models.IntegerField('like', default=0, validators=[MinValueValidator(0, '喜欢数不能小于0')])
    has_lyric = models.BooleanField('has_lyric', default=False)
    has_cover = models.BooleanField('has_cover', default=False)
    played = models.IntegerField('played', default=0, validators=[MinValueValidator(0, '播放量不能小于0')])
    # 歌单标签
    tag1 = models.CharField('tag1', max_length=30, default='')
    tag2 = models.CharField('tag2', max_length=30, default='')
    tag3 = models.CharField('tag3', max_length=30, default='')
    tag4 = models.CharField('tag4', max_length=30, default='')
    tag5 = models.CharField('tag5', max_length=30, default='')
    tag6 = models.CharField('tag6', max_length=30, default='')

    def detail_info(self):
        info = {'song_id': self.song_id, 'title': self.title, 'singer': self.singer, 'has_cover': self.has_cover,
                'has_lyric': self.has_lyric, 'introduction': self.introduction, 'uploader_id': self.uploader_id,
                'tag1': self.tag1, 'tag2': self.tag2, 'tag3': self.tag3, 'tag4': self.tag4, 'tag5': self.tag5,
                'tag6': self.tag6, 'like': self.like, 'played': self.played, 'cover_address': self.get_cover(),
                'lyric_address': self.get_lyric(), 'song_address': self.get_song(),
                'uploader_name': self.uploader.username, 'lyric_code': self.get_lyric_code()}
        return info

    def get_cover(self):
        if self.has_cover:
            prefix = 'cover/' + str(self.song_id)
            prefix = bucket.list_file(prefix)
            cover_addr = SONG_COVER_PREFIX + prefix
        else:
            cover_addr = SONG_DEFAULT_COVER
        return cover_addr

    def get_lyric(self):
        if self.has_lyric:
            lyric_addr = SONG_LYRIC_PREFIX + str(self.song_id) + '.lrc'
        else:
            lyric_addr = None
        return lyric_addr

    def get_song(self):
        prefix = 'song/' + str(self.song_id)
        prefix = bucket.list_file(prefix)
        song_addr = SONG_ADDRESS_PREFIX + prefix
        return song_addr

    def get_lyric_code(self):
        if not self.has_lyric:
            return None
        else:
            return get_code('https://' + self.get_lyric())

    def __str__(self):
        return self.title
