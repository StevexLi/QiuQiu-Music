from django.contrib import admin
from SongList.models import SongList, likeList


# Register your models here.
class SongListAdmin(admin.ModelAdmin):
    list_display = ('title', 'list_id', 'creator_id', 'sharable')
    ordering = ('list_id',)
    list_display_links = ('title',)
    search_fields = ['list_id', 'creator_id', 'title']
    list_per_page = 50
    list_editable = ('sharable',)
    filter_horizontal = ('content',)


class LikeListAdmin(admin.ModelAdmin):
    list_display = ('creator_id', '__str__')
    ordering = ('creator_id',)
    list_display_links = ('__str__',)
    list_per_page = 50
    filter_horizontal = ('content',)


admin.site.register(SongList, SongListAdmin)
admin.site.register(likeList, LikeListAdmin)
