from django.contrib import admin
from .models import (
Category,
Tag,
Post,
PostComment,
)


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['category', 'title', 'read_time']
    list_filter = ['category']
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title", )}


@admin.register(PostComment)
class AdminPostComment(admin.ModelAdmin):
    list_display = ['post']

