#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create by Pycharm
File        dennis_pyweb:celery.py
User        xieminliang
Create Date 2018/4/4 18:02

"""

from __future__ import absolute_import
import os
from django.conf import settings

# set the default Django conf module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
if settings.IS_USE_CELERY:
    from celery import Celery
    from django.conf import settings

    app = Celery('setting')

    # Using a string here means the worker will not have to
    # pickle the object when using Windows.
    app.config_from_object(settings)
    app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


    @app.task(bind=True)
    def debug_task(self):
        print('Request: {0!r}'.format(self.request))
