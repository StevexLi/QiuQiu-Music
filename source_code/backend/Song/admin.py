from django.contrib import admin
from Song.models import Song


# Register your models here.
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'song_id', 'singer', 'uploader_id')
    list_per_page = 50
    ordering = ('song_id',)
    search_fields = ('song_id', 'uploader_id', 'title', 'singer')


admin.site.register(Song, SongAdmin)
