from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import *


# Create your views here.
def index(request):
    return HttpResponse("Hello World")
