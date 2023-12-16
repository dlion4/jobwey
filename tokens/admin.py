from django.contrib import admin
from .models import TinyMceApiKey

# Register your models here.


@admin.register(TinyMceApiKey)
class TinyMceApiKeyAdmin(admin.ModelAdmin):
    list_display = ['key', 'is_active']

    