from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.main, name='main'),
    path('pages/about', views.about, name='about'),
    path('pages/blog', views.blog, name='blog'),
    path('pages/project', views.project, name='project'),
    path('pages/publications', views.publications, name='publications'),
    path('pages/contact', views.contact, name='contact'),

    path('pages/index/', views.main, name='main'),
    path('pages/pages/publications', views.publications, name='publications'),
    path('pages/pages/blog', views.blog, name='blog'),
    path('pages/pages/contact', views.contact, name='contact'),
    path('pages/pages/project', views.project, name='project'),
    path('pages/pages/about', views.about, name='about'),

    path('pages/<int:post_id>/about', views.about_2, name='about'),
    path('pages/<int:post_id>/publications', views.publications_2, name='publications'),
    path('pages/<int:post_id>/contact', views.contact_2, name='contact'),
    path('pages/<int:post_id>/blog', views.blog_2, name='blog'),
    path('pages/<int:post_id>/', views.blogdetails, name='blogdetails'),
    path('pages/<int:post_id>/project', views.project_2, name='project'),
    
    path('pages/project/<int:post_id>/', views.viewProject, name='viewProject'),
    path('pages/project/index', views.main, name='main'),
    path('pages/project/<int:post_id>/about', views.about_2, name='about'),
    path('pages/project/<int:post_id>/publications', views.publications_2, name='publications'),
    path('pages/project/<int:post_id>/contact', views.contact_2, name='contact'),
    path('pages/project/<int:post_id>/blog', views.blog_2, name='blog'),
    path('pages/project/<int:post_id>/project', views.project_2, name='project'),

]
