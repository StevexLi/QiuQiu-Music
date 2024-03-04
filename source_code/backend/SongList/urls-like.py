from django.urls import path
from SongList import views

urlpatterns = [
    path('add/', views.add_song_to_like),
    path('delete/', views.delete_song_from_like),
    path('get/', views.get_like_list),
    path('check/', views.check_song_in_like_list),
]