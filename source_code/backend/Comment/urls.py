from django.urls import path
from .views import add_comment, get_comment_info, delete_comment

urlpatterns = [
    path('add/', add_comment, name='add_comment'),
    path('get_info/', get_comment_info, name='get_comment_info'),
    path('delete/', delete_comment, name='delete_comment'),
]
