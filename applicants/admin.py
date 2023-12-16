from django.contrib import admin
from .models import Application

# Register your models here.
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = [
        "job",
        "profile",
        "full_name",
        "email_address",
        "phone_number",
        "is_active",
    ]


    