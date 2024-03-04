from django.contrib import admin
from User.models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ['groups', 'user_permissions']


admin.site.register(User, UserAdmin)
