from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return HttpResponse("welcome teachers")

def Services(request):
    return HttpResponse("Below are our services")

def About(request):
    return HttpResponse("welcome to our about page")
