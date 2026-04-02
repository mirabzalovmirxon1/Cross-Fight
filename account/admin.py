from django.contrib import admin
from .models import Account

@admin.register(Account)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role')