from django.db import models
from SongList.models import SongList
from Song.models import Song


# Create your models here.
class Complain(models.Model):
    complainer = models.ForeignKey(to='User.User', on_delete=models.CASCADE)
    type = models.BooleanField(null=False)  # True => song, False => list
    obj_id = models.IntegerField(null=False)
    content = models.CharField(max_length=200)

    def obj_delete(self):
        if self.type:
            obj = Song.objects.get(song_id=self.obj_id)
            obj.delete()
        else:
            obj = SongList.objects.get(list_id=self.obj_id)
            obj.sharable = False

    def get_obj(self):
        if self.type:
            obj = Song.objects.get(song_id=self.obj_id)
        else:
            obj = SongList.objects.get(list_id=self.obj_id)
        return obj

    def get_cover_address(self):
        if self.type:
            obj = Song.objects.get(song_id=self.obj_id)
        else:
            obj = SongList.objects.get(list_id=self.obj_id)
        addr = obj.get_cover()
        return addr

    def get_uploader_id(self):
        if self.type:
            obj = Song.objects.get(song_id=self.obj_id)
            res_id = obj.uploader_id
        else:
            obj = SongList.objects.get(list_id=self.obj_id)
            res_id = obj.creator_id
        return res_id

    def detail_info(self):
        info = {
            'id': self.id,
            'complainer_id': self.complainer.uid,
            'complainer_name': self.complainer.username,
            'type': self.type,
            'obj_id': self.obj_id,
            'obj_cover_address': self.get_cover_address(),
            'obj_uploader_id': self.get_uploader_id(),
            'content': self.content,
        }
        return info
