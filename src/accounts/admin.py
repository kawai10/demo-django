from django.contrib import admin

from src.accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "password", "email", "created_at", "updated_at")
