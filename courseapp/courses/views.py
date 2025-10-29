from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(req):
    return HttpResponse('Home Page')

def courses(req):
    return HttpResponse('Courses Page')