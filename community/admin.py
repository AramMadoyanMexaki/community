from django.contrib import admin
from .models import Author, Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "category", "created_at", "title")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
