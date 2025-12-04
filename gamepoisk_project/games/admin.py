from django.contrib import admin
from .models import Game, Comment
from django.utils.html import format_html

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'developer', 'publisher', 'image_tag')
    search_fields = ('title', 'genre', 'developer', 'publisher')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:100px;" />', obj.image.url)
        return '(No image)'
    image_tag.short_description = 'Image Preview'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'game', 'created_at')
    search_fields = ('author__username', 'content')
