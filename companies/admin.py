from django.contrib import admin
from .models import (Company, Job)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        "company",
        "title",
        "type",
        "positions",
        "location",
        "min_salary",
        "max_salary",
        "createdAt",
        "updatedAt",
    ]
    list_filter = ['company',"type","location",]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['company', 'title', 'location']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name',"jobs_count","positions_avg", "createdAt","updatedAt"]
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name", )}


