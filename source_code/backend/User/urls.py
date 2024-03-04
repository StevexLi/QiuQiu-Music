from django.urls import path

from User import views

urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('get_info/', views.get_basic_info),
    path('get_list_a/', views.get_song_list_all),
    path('get_list_s/', views.get_list_sharable),
    path('get_song/', views.get_uploaded_song),
    path('change_info/', views.update_basic_info),
    path('login_test/', views.login_test),
]