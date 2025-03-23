from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.user", default="Unknown")

    class Meta: 
        model = Post
        fields = ['id', 'title', 'author', 'created_at', 'text', 'image']
