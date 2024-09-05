from django.shortcuts import render
from django.http import HttpResponse
# from .tasks import test_task
# from decouple import config
# Create your views here.

def index(request):
    # test_task.delay()

    return HttpResponse(f'HHM......Hello World! This is CN Django Test.By - Lav aa.....web hooks test lav webhook testing 123 - lav2828')