from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sidequestapi.settings.dev')

celery = Celery('sidequestapi')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()
