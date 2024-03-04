from django.urls import path, include
from SongList import views

urlpatterns = [
    # song list CURD
    path('create/', views.create_list),
    path('delete/', views.delete_list),
    path('get/', views.get_list_info),
    path('update/', views.update_list_info),
    path('add/', views.add_song_to_list),
    path('remove/', views.remove_song_from_list),
    # song list other operation
    path('share/', views.share_song_list),
    path('complain/', views.complain_song_list),
    # like list operation
    path('like/', include('SongList.urls-like')),
]
