from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.main, name='main'),
    path('pages/about.html', views.about, name='about'),
    path('pages/blog.html', views.blog, name='blog'),
    path('pages/project.html', views.project, name='project'),
    path('pages/publications.html', views.publications, name='publications'),
    path('pages/contact.html', views.contact, name='contact'),

    path('pages/index.html', views.main, name='main'),
    path('pages/pages/publications.html', views.publications, name='publications'),
    path('pages/pages/blog.html', views.blog, name='blog'),
    path('pages/pages/contact.html', views.contact, name='contact'),
    path('pages/pages/project.html', views.project, name='project'),
    path('pages/pages/about.html', views.about, name='about'),

    path('pages/<int:post_id>/about.html', views.about_2, name='about'),
    path('pages/<int:post_id>/publications.html', views.publications_2, name='publications'),
    path('pages/<int:post_id>/contact.html', views.contact_2, name='contact'),
    path('pages/<int:post_id>/blog.html', views.blog_2, name='blog'),
    path('pages/<int:post_id>/', views.blogdetails, name='blogdetails'),
    path('pages/<int:post_id>/project.html', views.project_2, name='project'),
    path('pages/project<int:post_id>/', views.viewProject, name='viewProject'),

]
