from __future__ import absolute_import
import os
from celery import Celery
import django
django.setup()

from product.models import Product, StrategyProduct
from strategy.models import Strategy

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

@app.task
def first_task():
    print("Hello, World!")


# @app.task
# def strategy_product(product_id, strategy_id):
