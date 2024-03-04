from django.urls import path
from Complain import views

urlpatterns = [
    path('get/', views.get_complain),
    path('create/', views.create_complain),
    path('execute/', views.execute_complain)
]