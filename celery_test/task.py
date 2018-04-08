#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create by Pycharm
File        dennis_pyweb:task.py
User        xieminliang
Create Date 2018/4/8 10:42

"""

from __future__ import absolute_import, unicode_literals
from  celery import task
import time
from .mail import Mail


@task()
def test(name):
    for i in range(1, 10):
        print('hello {0}--{1}'.format(name, i))
        time.sleep(1)


@task()
def mail_test():
    mail = Mail()
    mailsubject = 'xieminliang celer test2'
    message = 'hello, this is test 5'
    mail.send_mail(['xxx@qq.com', ], mailsubject, message)



