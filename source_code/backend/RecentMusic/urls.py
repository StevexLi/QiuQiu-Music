from django.urls import path
from .views import recent_played_songs, record_play

urlpatterns = [
    path('get/', recent_played_songs, name='recent_played_songs'),
    path('add/', record_play, name='record_play'),
]
