from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('project/', views.project, name='project'),
    path('publications/', views.publications, name='publications'),
    path('contact/', views.contact, name='contact'),

    path('blog/<int:post_id>/', views.blogdetails, name='blogdetails'),
    path('project/<int:post_id>/', views.viewProject, name='viewProject'),

    path('search/', views.search, name='search'),
    path('project_search/', views.project_search, name='project_search'),


]
