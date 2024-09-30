# notification_app/celery.py

from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notification_app.settings')

app = Celery('notification_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
