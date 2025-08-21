from django.shortcuts import render
from . models import Profile, Project, Publications, Blog, Contact, skill

# Create your views here.
def home(request):
    profile = Profile.objects.first()
    link = Contact.objects.first()
    return render(request, 'index.html', {'profile': profile, 'link': link })

def main(request):
    profile = Profile.objects.first()
    link = Contact.objects.first()
    return render(request, 'index.html', {'profile': profile, 'link': link})

def about(request):
    about = Profile.objects.first()
    experience = skill.objects.all()
    return render(request, 'pages/about.html', {'about': about, 'experience': experience})

def blog(request):
    return render(request, 'pages/blog.html')

def blogdetails(request):
    return render(request, 'pages/blogDetails.html')

def project(request):
    return render(request, 'pages/project.html')

def viewProject(request):
    return render(request, 'pages/viewProject.html')

def publications(request):
    publication = Publications.objects.all()
    return render(request, 'pages/publications.html', {'publication': publication})

def contact(request):
    return render(request, 'pages/contact.html')