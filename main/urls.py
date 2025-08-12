from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('pages/about.html', views.about, name='about'),
    path('pages/blog.html', views.blog, name='blog'),
]
