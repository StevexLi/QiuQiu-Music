"""PopstarMusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:from django.urls import path, include
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include("User.urls")),
    path('api/song/', include("Song.urls")),
    path('api/songlist/', include("SongList.urls")),
    path('api/search/', include("Search.urls")),
    path('api/describe/', include("DescribeList.urls")),
    path('api/comment/', include("Comment.urls")),
    path('api/history/', include("RecentMusic.urls")),
    path('api/notification/', include("Notifications.urls")),
    path('api/complain/', include("Complain.urls")),
]
