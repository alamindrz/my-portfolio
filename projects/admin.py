# projects/admin.py
from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Project
from django.utils.html import format_html

@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ['title', 'image_preview', 'created_at', 'project_link']
    list_filter = ['created_at']
    search_fields = ['title', 'description']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "No Image"
    image_preview.short_description = 'Preview'
    
    def project_link(self, obj):
        if obj.project_url:
            return format_html(
                '<a href="{}" target="_blank">🔗 View</a>',
                obj.project_url
            )
        return "No Link"
    project_link.short_description = 'Link'