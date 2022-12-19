from __future__ import absolute_import
import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

@app.task
def first_task():
    print("Hello, World!")


# @app.task
# def strategy_product(product_id, strategy_id):
