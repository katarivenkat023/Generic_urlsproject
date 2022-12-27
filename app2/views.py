from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def third(request):
    return HttpResponse('<h1>this is my third views</h1>')
