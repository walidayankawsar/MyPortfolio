from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def main(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'pages/about.html')

def blog(requets):
    return render(requets, 'pages/blog.html')

def project(request):
    return render(request, 'pages/project.html')