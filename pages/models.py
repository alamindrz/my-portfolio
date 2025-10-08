from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from utils.image_utils import compress_image, create_thumbnail



class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=250)
    subtitle = models.CharField(max_length=255, blank=True)
    content = RichTextField(config_name='default') 
    header_image = models.ImageField(upload_to='blog/headers/', blank=True)
    header_thumbnail = models.ImageField(upload_to='blog/thumbnails/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    meta_description = models.TextField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # Compress header image using utility function
        if self.header_image:
            self.header_image = compress_image(
                self.header_image, 
                quality=80, 
                max_size=(1200, 800)  # Larger size for blog headers
            )
            
        # Create header thumbnail using utility function
        if self.header_image and not self.header_thumbnail:
            self.header_thumbnail = create_thumbnail(
                self.header_image, 
                size=(600, 400), 
                quality=70
            )
            
        if self.status == 'published' and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
