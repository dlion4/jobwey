from django.contrib import admin
from .models import Testimony
from .forms import TestimonyAdminForm
# Register your models here.


@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    form = TestimonyAdminForm
    list_display = ['profile', 'is_positive']
    list_filter = ['profile', ]
    actions = ("is_positive_testimony", )

    @admin.action(description="Is moderated")
    def is_positive_testimony(self, request, queryset):
        queryset.update(is_positive=True)


