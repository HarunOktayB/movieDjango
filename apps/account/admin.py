from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

admin.site.site_header = "Kullanıcı Yönetim Paneli"

class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['is_staff', 'is_superuser', 'is_active']

# Unregister the default User admin and register the new UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

