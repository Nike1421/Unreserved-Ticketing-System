from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ['username', 'name', 'date_joined', 'last_login', 'is_admin', 'is_staff']
    search_fields = ['name', 'username']
    readonly_fields = ['date_joined', 'last_login']
    ordering = ('username',)
    filter_horizontal = []
    list_filter = []
    fieldsets = []

admin.site.register(Account, AccountAdmin)
