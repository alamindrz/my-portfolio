# wsgi_pa.py
import os
import sys

path = '/home/alamindarazo/my-portfolio'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_project.settings_pa'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()