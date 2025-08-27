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
    project = Project.objects.all()
    links = Contact.objects.first()
    return render(request, 'pages/project.html', {'link': links, 'projects': project})

def project_2(request, post_id):
    project = Project.objects.all()
    links = Contact.objects.first()
    return render(request, 'pages/project.html', {'link': links, 'projects': project})

def viewProject(request, post_id):
    project = get_object_or_404(Project, id=post_id)
    links = Contact.objects.first()
    return render(request, 'pages/viewProject.html', {'projects': project, 'link': links})

def publications(request):
    links = Contact.objects.first()
    publication = Publications.objects.all()
    return render(request, 'pages/publications.html', {'publication': publication, 'link': links})

def publications_2(request, post_id):
    links = Contact.objects.first()
    publication = Publications.objects.all()
    return render(request, 'pages/publications.html', {'publication': publication, 'link': links})

# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()  # ডাটাবেজে save হবে

            # ইমেইল পাঠানো
            subject = "New Contact Message"
            message = f"""
            Name: {contact.name}
            Phone: {contact.phone}
            Message:
            {contact.message}
            """
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            messages.success(request, "✅ Your message has been sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "❌ Please correct the errors below.")
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})

def contact_2(request, post_id):
    page = Contact.objects.first()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            subject = "New Contact Message"
            message = f"""
            Name: {contact.name}
            Phone: {contact.phone}
            Message:
            {contact.message}
            """
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            messages.success(request, "✅ Your message has been sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "❌ Please correct the errors below.")
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'page':page, 'form': form})