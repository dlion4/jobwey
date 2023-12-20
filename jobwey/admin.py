from django.contrib import admin
from .models import Service, Visa
# Register your models here.

@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ["title","country"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Visa)
class AdminService(admin.ModelAdmin):
    list_display = ["country"]
    prepopulated_fields = {"slug": ("country",)}
