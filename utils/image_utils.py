# utils/image_utils.py
import os
from io import BytesIO
from PIL import Image
from django.core.files import File

def compress_image(image, quality=70, max_size=(800, 600), format='JPEG'):
    """
    Compress and optimize image with size constraints
    Reusable across all models
    """
    try:
        im = Image.open(image)
        
        # Convert to RGB if necessary for JPEG
        if format == 'JPEG' and im.mode in ('RGBA', 'P'):
            im = im.convert('RGB')
        
        # Resize if image is too large
        if max_size:
            im.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        # Compress
        im_io = BytesIO()
        im.save(im_io, format, quality=quality, optimize=True)
        compressed_image = File(im_io, name=image.name)
        return compressed_image
    except Exception as e:
        # Return original image if compression fails
        print(f"Image compression failed: {e}")
        return image

def create_thumbnail(image, size=(400, 300), quality=60, format='JPEG'):
    """
    Create a thumbnail version from an image
    Reusable across all models
    """
    try:
        im = Image.open(image)
        
        # Convert to RGB if necessary for JPEG
        if format == 'JPEG' and im.mode in ('RGBA', 'P'):
            im = im.convert('RGB')
            
        im.thumbnail(size, Image.Resampling.LANCZOS)
        
        thumb_io = BytesIO()
        im.save(thumb_io, format, quality=quality, optimize=True)
        thumbnail = File(thumb_io, name=f'thumb_{image.name}')
        return thumbnail
    except Exception as e:
        print(f"Thumbnail creation failed: {e}")
        return None

def get_image_upload_path(instance, filename, base_folder):
    """
    Generate consistent file path for images across models
    """
    # Get model name for folder organization
    model_name = instance.__class__.__name__.lower()
    ext = filename.split('.')[-1]
    filename = f'main.{ext}'
    return os.path.join(base_folder, model_name, instance.title, filename)