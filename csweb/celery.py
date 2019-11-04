from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
# Set de django setting module for the celery program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cornershop_test.settings')
app = Celery('MenuApp') # create the celery app
app.config_from_object('django.conf:settings', namespace='CELERY') 
app.autodiscover_tasks() 
app.conf.update(
    BROKER_URL = 'amqp://localhost', #The task will be managed by rabbitMQ
)