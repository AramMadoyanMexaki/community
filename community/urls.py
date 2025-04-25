from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('api/post/', get_posts, name="get_posts"),
    path('blog/', blog, name="blog"),
    path('details/<int:id>/', details, name="detail"),
    path('about-us/', about, name="about-us"),
    path('contact/', contact, name='contact'),
    path('privacy-policy/', policy, name='privacy'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
