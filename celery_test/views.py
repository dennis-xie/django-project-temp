from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .task import test


def celery_test(request):
    test.delay('dennis')
    return HttpResponse('done')


from .task import mail_test


def celery_test2(request):
    mail_test.delay()
    return HttpResponse('send mail success')