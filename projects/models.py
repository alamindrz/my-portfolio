# projects/models.py
import os
from django.db import models
from django.conf import settings
from utils.image_utils import compress_image, create_thumbnail, get_image_upload_path

def project_image_path(instance, filename):
    """Generate file path for project images using utility function"""
    return get_image_upload_path(instance, filename, settings.PROJECTS_MEDIA_DIR)

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('mobile', 'Mobile Apps'),
        ('design', 'UI/UX Design'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to=project_image_path)
    thumbnail = models.ImageField(upload_to=project_image_path, blank=True, null=True)
    project_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web')
    
    def get_category_badge_color(self):
        """Custom method to return different badge colors based on category"""
        color_map = {
            'web': 'bg-blue-100 text-blue-600',
            'mobile': 'bg-green-100 text-green-600',
            'design': 'bg-purple-100 text-purple-600',
            'other': 'bg-gray-100 text-gray-600',
        }
        return color_map.get(self.category, 'bg-gray-100 text-gray-600')
    
    def get_category_icon(self):
        """Custom method to return icons for categories"""
        icon_map = {
            'web': '🌐',
            'mobile': '📱',
            'design': '🎨',
            'other': '📁',
        }
        return icon_map.get(self.category, '📁')
    
    # REMOVED: compress_image and create_thumbnail methods (now using utilities)
    
    def save(self, *args, **kwargs):
        # Compress main image before saving using utility function
        if self.image:
            self.image = compress_image(self.image, quality=70, max_size=(800, 600))
            
        # Create thumbnail if it doesn't exist using utility function
        if self.image and not self.thumbnail:
            self.thumbnail = create_thumbnail(self.image, size=(400, 300), quality=60)
            
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_image_url(self):
        """Safe method to get image URL"""
        if self.image:
            return self.image.url
        return '/static/images/default-project.jpg'

    def get_thumbnail_url(self):
        """Safe method to get thumbnail URL"""
        if self.thumbnail:
            return self.thumbnail.url
        elif self.image:
            return self.image.url
        return '/static/images/default-project-thumb.jpg'