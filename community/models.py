from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=122)
    picture = models.ImageField(upload_to="post/pictures/", blank=True, null=True)
    text = models.TextField(null=True)

    def __str__(self):
        return "{}, {}".format(self.author, self.title)
    

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

