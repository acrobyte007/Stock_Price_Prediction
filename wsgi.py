import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')  # Update this if your settings file is named differently

application = get_wsgi_application()
