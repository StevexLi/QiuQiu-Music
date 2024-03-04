from django.urls import path
from .views import create_notification, get_notifications
urlpatterns = [
    path('create/', create_notification, name='create_notification'),
    path('get/', get_notifications, name='get_notifications'),
]

