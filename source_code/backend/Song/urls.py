from django.urls import path
from Song import views

urlpatterns = [
    path('upload/', views.upload_song),
    path('get_info/', views.get_song_info),
    path('delete/', views.delete_song),
    path('update/', views.update_song),
    path('played/', views.increase_played),
]