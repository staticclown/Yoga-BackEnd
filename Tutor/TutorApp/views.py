from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse


def home(request):
    return HttpResponse('hi')

# Create your views here.
