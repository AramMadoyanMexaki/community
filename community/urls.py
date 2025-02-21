from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('blog/', blog, name="blog"),
    path('details/', details, name="detail"),
]
