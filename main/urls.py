from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.main, name='main'),
    path('pages/about.html', views.about, name='about'),
    path('pages/blog.html', views.blog, name='blog'),
    path('pages/<int:post_id>/', views.blogdetails, name='blogdetails'),
    path('pages/project.html', views.project, name='project'),
    path('pages/viewProject.html', views.viewProject, name='viewProject'),
    path('pages/publications.html', views.publications, name='publications'),
    path('pages/contact.html', views.contact, name='contact'),

    path('pages/index.html', views.main, name='main'),
]
