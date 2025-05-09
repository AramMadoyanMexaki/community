from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=122)
    image = models.ImageField(upload_to="post/image/", blank=True, null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return "{}, {}".format(self.author, self.title)
    

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="categoria/icons", blank=True, null=False)
    
    def __str__(self):
        return self.name

