#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create by Pycharm
File        dennis_pyweb:prod.py
User        xieminliang
Create Date 2018/4/4 17:45

"""
from .base import *


DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'xxx',         #这里一定要写你数据库的名字，要先建库
        'USER': 'root',
        'PASSWORD': 'xxx',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
    }
}


LOG_LEVEL = 'ERROR'

