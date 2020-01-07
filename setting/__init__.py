from __future__ import absolute_import
from django.conf import settings

if settings.IS_USE_CELERY:
    from .celery import  app as celery_app
