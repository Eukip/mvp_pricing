from __future__ import absolute_import
import os
from celery import Celery, shared_task


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

celery_app = Celery("config")

celery_app.config_from_object("django.conf:settings", namespace="CELERY")

celery_app.autodiscover_tasks()

@shared_task
def first_task():
    print("Hello, World!")
