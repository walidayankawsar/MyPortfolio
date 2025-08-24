from django.shortcuts import render, get_object_or_404
from . models import Profile, Project, Publications, Blog, Contact, skill

# Create your views here.
def home(request):
    profile = Profile.objects.first()
    link = Contact.objects.first()
    return render(request, 'index.html', {'profile': profile, 'link': link })

def main(request):
    profile = Profile.objects.first()
    links = Contact.objects.first()
    return render(request, 'index.html', {'profile': profile, 'link': links})

def about(request):
    links = Contact.objects.first()
    about = Profile.objects.first()
    experience = skill.objects.all()
    return render(request, 'pages/about.html', {'about': about, 'experience': experience, 'link': links})

def about_2(request, post_id):
    links = Contact.objects.first()
    about = Profile.objects.first()
    experience = skill.objects.all()
    return render(request, 'pages/about.html', {'about': about, 'experience': experience, 'link': links})

def blog(request):
    posts = Blog.objects.all()
    return render(request, 'pages/blog.html', {'posts': posts})

def blog_2(request, post_id):
    posts = Blog.objects.all()
    return render(request, 'pages/blog.html', {'posts': posts})

def blogdetails(request, post_id):
    links = Contact.objects.first()
    post = get_object_or_404(Blog, id=post_id)
    return render(request, 'pages/blogDetails.html', {'post': post, 'link': links})

def project(request):
    return render(request, 'pages/project.html')

def project_2(request, post_id):
    return render(request, 'pages/project.html')

def viewProject(request):
    return render(request, 'pages/viewProject.html')

def viewProject_2(request, post_id):
    return render(request, 'pages/viewProject.html')

def publications(request):
    links = Contact.objects.first()
    publication = Publications.objects.all()
    return render(request, 'pages/publications.html', {'publication': publication, 'link': links})

def publications_2(request, post_id):
    links = Contact.objects.first()
    publication = Publications.objects.all()
    return render(request, 'pages/publications.html', {'publication': publication, 'link': links})

def contact(request):
    return render(request, 'pages/contact.html')

def contact_2(request, post_id):
    page = Contact.objects.first()
    return render(request, 'pages/contact.html', {'page':page})