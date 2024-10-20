from celery import shared_task
from django.utils import timezone
from .models import Notification
from django.contrib.auth.models import User

@shared_task
def send_reminder():
    users = User.objects.all()
    for user in users:
        Notification.objects.create(user=user, message="Don't forget to check your pet's appointments!")
