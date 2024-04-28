import datetime

from django.shortcuts import render
from django.http import HttpResponse


def date_now(request):
    return HttpResponse(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
