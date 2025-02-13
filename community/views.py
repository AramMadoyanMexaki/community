from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def blog(request):
    return render(request, "blog.html")