from django.db import models

from Tool.bucket import bucket
from properties import SONG_DEFAULT_COVER, SONG_COVER_PREFIX, DEFAULT_LIKE_COVER


# Create your models here.
class SongList(models.Model):
    # 歌单基本信息
    list_id = models.BigAutoField('list_id', primary_key=True, auto_created=True)
    title = models.CharField('title', max_length=50)
    has_cover = models.BooleanField('has_cover', default=False)
    creator = models.ForeignKey(to='User.User', to_field='uid', on_delete=models.CASCADE)
    content = models.ManyToManyField(to='Song.Song', default=None)
    sharable = models.BooleanField('sharable', default=False)
    introduction = models.CharField(max_length=200, default='暂无介绍')
    # 歌单标签
    tag1 = models.CharField('tag1', max_length=30, default='')
    tag2 = models.CharField('tag2', max_length=30, default='')
    tag3 = models.CharField('tag3', max_length=30, default='')
    tag4 = models.CharField('tag4', max_length=30, default='')
    tag5 = models.CharField('tag5', max_length=30, default='')
    tag6 = models.CharField('tag6', max_length=30, default='')

    def detail_info(self):
        info = {
            'list_id': self.list_id,
            'title': self.title,
            'has_cover': self.has_cover,
            'creator_id': self.creator_id,
            'creator_name': self.creator.username,
            'introduction': self.introduction,
            'sharable': self.sharable,
            'tag1': self.tag1,
            'tag2': self.tag2,
            'tag3': self.tag3,
            'tag4': self.tag4,
            'tag5': self.tag5,
            'tag6': self.tag6,
        }
        songs = list(self.content.all())
        res = []
        for _ in songs:
            res.append(_.detail_info())
        info['cover_address'] = self.get_cover()
        info['content'] = res
        count = len(songs)
        info['total'] = count
        return info

    def get_cover(self):
        if not self.has_cover:
            cover_addr = SONG_DEFAULT_COVER
        else:
            prefix = 'list_cover/' + str(self.list_id)
            prefix = bucket.list_file(prefix)
            cover_addr = SONG_COVER_PREFIX + prefix
        return cover_addr

    def __str__(self):
        return self.title


class likeList(models.Model):
    # 喜欢列表基本信息
    creator = models.OneToOneField(to='User.User', to_field='uid', primary_key=True,
                                   on_delete=models.CASCADE)
    content = models.ManyToManyField(to='Song.Song', default=None)

    def detail_info(self):
        info = {
            'creator_id': self.creator_id,
            'cover_address': self.get_cover_address(),
        }
        songs = list(self.content.all())
        songs.reverse()
        resp = []
        for _ in songs:
            resp.append(_.detail_info())
        info['content'] = resp
        count = len(songs)
        info['total'] = count
        return info

    def get_cover_address(self):
        return DEFAULT_LIKE_COVER

    def __str__(self):
        return self.creator.username
