from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "category", "created_at", "title")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
