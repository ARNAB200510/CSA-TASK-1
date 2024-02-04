"""
WSGI config for Food_Delivery_App_By_CSA project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Food_Delivery_App_By_CSA.settings')

application = get_wsgi_application()
