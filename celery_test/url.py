#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create by Pycharm
File        dennis_pyweb:url.py
User        xieminliang
Create Date 2018/4/8 10:44

"""
from django.conf.urls import url

from celery_test import views


urlpatterns = [

    url(r'^celery', views.celery_test, name='celery_test'),
    url(r'^test2', views.celery_test2, name='celery_test2'),


]