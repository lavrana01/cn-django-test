from django.shortcuts import render
from django.http import HttpResponse
# from .tasks import test_task
# from decouple import config
# Create your views here.

def index(request):
    # test_task.delay()

    return HttpResponse(f'LLM....CodeDeploy with Jenkins succesfull deployment! This is Jenkins Django Test.By - Lav aa.....CI CD test by lav - lav2828')