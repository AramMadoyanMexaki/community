from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('blog/', blog, name="blog"),
    path('details/', details, name="detail"),
    path('about-us/', about, name="about-us"),
    path('contact/', contact, name='contact'),
    path('privacy-policy/', policy, name='privacy'),
]
