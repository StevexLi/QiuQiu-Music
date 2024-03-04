from django.urls import path
from DescribeList import views

urlpatterns = [
    path('add/', views.add_to_describe_list),
    path('remove/', views.remove_from_describe_list),
    path('get/', views.get_describer_list),
    path('check/', views.check_describer_in_user_list),
]