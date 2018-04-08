#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create by Pycharm
File        dennis_pyweb:mail.py
User        xieminliang
Create Date 2018/1/24 12:53

"""
import smtplib
from email.mime.text import MIMEText


class Mail(object):
	def __init__(self):
		self.__mailhost = 'smtp.exmail.qq.com'
		self.__user = 'xxx.com'
		self.__pass = 'xxx'
		self.__postfix = 'xxx.com'
		self.__port = '465'
	def send_mail(self, to_list, subject, content):
		msg = MIMEText(content, 'html', 'utf-8')
		msg['Subject'] = subject
		msg['From'] = self.__postfix
		msg['to'] = ','.join(to_list)

		try:
			server = smtplib.SMTP(self.__mailhost)
			server.login(self.__user, self.__pass)
			server.sendmail(self.__postfix, to_list, msg.as_string())
			server.quit
		except Exception as e:
			print(str(e))
			return False