from django.shortcuts import render
from . models import Profile

# Create your views here.
def home(request):
    profile = Profile.objects.all()
    return render(request, 'index.html', {'pic': profile})

def main(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'pages/about.html')

def blog(requets):
    return render(requets, 'pages/blog.html')

def project(request):
    return render(request, 'pages/project.html')

def publications(request):
    return render(request, 'pages/publications.html')

def contact(request):
    return render(request, 'pages/contact.html')