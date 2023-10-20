from django.contrib import admin
from .models import TelegramUser


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'user_id']
    search_fields = ['user_id']

admin.site.register(TelegramUser, TelegramUserAdmin)
