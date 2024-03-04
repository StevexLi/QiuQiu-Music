from django.contrib import admin
from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('user__username', 'message')
    ordering = ('-created_at',)


admin.site.register(Notification, NotificationAdmin)
