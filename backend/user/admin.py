from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'is_staff')