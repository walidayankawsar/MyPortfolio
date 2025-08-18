from django.shortcuts import render
from . models import Profile

# Create your views here.
def home(request):
    profile = Profile.objects.first()
    return render(request, 'index.html', {'pic': profile})

def main(request):
    profile = Profile.objects.first()
    return render(request, 'index.html', {'pic': profile})

def about(request):
    return render(request, 'pages/about.html')

def blog(request):
    return render(request, 'pages/blog.html')

def blogdetails(request):
    return render(request, 'pages/blogDetails.html')

def project(request):
    return render(request, 'pages/project.html')

def viewProject(request):
    return render(request, 'pages/viewProject.html')

def publications(request):
    return render(request, 'pages/publications.html')

def contact(request):
    return render(request, 'pages/contact.html')