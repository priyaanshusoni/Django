from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(req):
    return HttpResponse('Hello ! This is homepage' )


def about(req):
    return HttpResponse("This is About Page")