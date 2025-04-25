from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import PostSerializer


def index(request):
    return render(request, "index.html")


@api_view(["GET"])
def get_posts(request):
    posts = Post.objects.all().order_by("-created_at")

    data = {
        "all_posts": PostSerializer(posts, many=True).data,
    }

    return Response(data)


def blog(request):
    posts = Post.objects.all()

    context = {
        "posts": posts,
    }
    
    return render(request, "blog.html", context)

def details(request, id):
    post = get_object_or_404(Post, id=id)
    all_posts = Post.objects.all()

    context = {
        "post": post,
        "all_posts": all_posts,
    }

    return render(request, "details.html", context)

def about(request):
    return render(request, "about-us.html")

def contact(request):
    return render(request, "contact.html")

def policy(request):
    return render(request, "privacy-policy.html")