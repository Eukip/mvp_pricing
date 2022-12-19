from __future__ import absolute_import, unicode_literals

import django
django.setup()

from .celery import app as celery_app
from config.celery import app as celery_app

__all__ = ("celery_app", )