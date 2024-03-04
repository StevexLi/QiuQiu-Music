from django.urls import path
from Search import views

urlpatterns = [
    path('song_name/', views.search_song_by_name),
    path('list_name/', views.search_list_by_name),
    path('song_tag/', views.search_song_by_tag),
    path('list_tag/', views.search_list_by_tag),
    path('random/', views.random_recommend),
]