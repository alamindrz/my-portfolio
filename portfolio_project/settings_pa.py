# settings_pa.py (or add to your existing settings)
import os
from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['alamindarazo.pythonanywhere.com', 'localhost', '127.0.0.1']

# Database - PythonAnywhere provides MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# HTTPS settings
SECURE_SSL_REDIRECT = False  # PythonAnywhere handles SSL
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False