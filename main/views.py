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
    abouts = Profile.objects.first()
    experience = skill.objects.all()
    return render(request, 'pages/about.html', {'about': abouts, 'experience': experience, 'link': links})

def about_2(request, post_id):
    links = Contact.objects.first()
    abouts = Profile.objects.first()
    experience = skill.objects.all()
    return render(request, 'pages/about.html', {'about': abouts, 'experience': experience, 'link': links})

def blog(request):
    links = Contact.objects.first()
    posts = Blog.objects.all()
    return render(request, 'pages/blog.html', {'posts': posts, 'link': links})

def blog_2(request, post_id):
    links = Contact.objects.first()
    posts = Blog.objects.all()
    return render(request, 'pages/blog.html', {'posts': posts, 'link': links})

def blogdetails(request, post_id):
    links = Contact.objects.first()
    post = get_object_or_404(Blog, id=post_id)
    return render(request, 'pages/blogDetails.html', {'post': post, 'link': links})

def project(request):
    projects = Project.objects.all()
    links = Contact.objects.first()
    return render(request, 'pages/project.html', {'link': links, 'posts': projects})

def project_2(request, post_id):
    projects = Project.objects.all()
    links = Contact.objects.first()
    return render(request, 'pages/project.html', {'link': links, 'posts': projects})

def viewProject(request, post_id):
    projects = get_object_or_404(Project, id=post_id)
    return render(request, 'pages/viewProject.html', {'posts': projects})

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