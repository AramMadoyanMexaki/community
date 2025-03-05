from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def blog(request):
    return render(request, "blog.html")

def details(request):
    return render(request, "details.html")

def about(request):
    return render(request, "about-us.html")

def contact(request):
    return render(request, "contact.html")

def policy(request):
    return render(request, "privacy-policy.html")