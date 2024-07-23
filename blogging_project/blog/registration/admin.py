# admin.py
from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')  # Display these fields in the list view


admin.site.register(Post, PostAdmin)
