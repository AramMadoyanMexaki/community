from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import PostSerializer


def index(request):
    return render(request, "index.html")


@api_view(["GET"])
def get_posts(request):
    featured_post = Post.objects.filter(is_featured=True).first()
    posts = Post.objects.all().order_by("-created_at")

    data = {
        "featured_post": PostSerializer(featured_post).data if featured_post else None,
        "all_posts": PostSerializer(posts, many=True).data,
    }

    return Response(data)


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