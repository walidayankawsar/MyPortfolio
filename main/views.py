from django.shortcuts import render, get_object_or_404
from . models import Profile, Project, Publications, Blog, Contact, skill, Education
from django.db.models import Q

# Create your views here.
def home(request):
    profile = Profile.objects.first()
    link = Contact.objects.first()
    return render(request, 'index.html', {'profile': profile, 'link': link })

def about(request):
    links = Contact.objects.first()
    abouts = Profile.objects.first()
    experience = skill.objects.all()
    edu = Education.objects.all()
    return render(request, 'pages/about.html', {'about': abouts, 'experience': experience, 'link': links, 'edu': edu})

def blog(request):
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


def viewProject(request, post_id):
    project = get_object_or_404(Project, id=post_id)
    links = Contact.objects.first()
    return render(request, 'pages/viewProject.html', {'projects': project, 'link': links})

def publications(request):
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


def search(request):
    link = Contact.objects.first()
    query = request.GET.get('q')
    results = []
    if query:
        results = Blog.objects.filter(
            Q(name__icontains=query) |
            Q(tag__Tag_name__icontains=query)
        ).distinct()
    return render(request, 'pages/blog_search.html', {'results': results, 'query': query, 'links': link})


def project_search(request):
    link = Contact.objects.first()
    query = request.GET.get('q')
    results =[]
    if query:
        results = Project.objects.filter(
            Q(project_name__icontains=query) |
            Q(tag__Tag_name__icontains=query)
        ).distinct()
    return render(request, 'pages/project_search.html', {'results': results, 'query': query, 'links': link})
    