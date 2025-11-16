from django.db import models

# Create your models here.
class Profile(models.Model):
    picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    graduate = models.CharField(max_length=100, blank=True, null=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class skill(models.Model):
    work = models.CharField(max_length=100, blank=True, null=True)
    work_description = models.TextField(blank=True, null=True)
    work_date = models.DateField(blank=True, null=True)

class Education(models.Model):
    achievements = models.CharField(max_length=100, blank=True, null=True)
    education_description = models.TextField(blank=True, null=True)
    education_date = models.DateField(blank=True, null=True)

class Tags(models.Model):
    Tag_name = models.CharField(max_length=100, unique=True, blank=True, null=True)

class Project(models.Model):
    project_name = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(upload_to='picture of project/', blank=True, null=True)
    tag = models.ManyToManyField(Tags, related_name="posts", blank=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    website_link = models.URLField(blank=True, null=True)

class Publications(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    authors = models.TextField(max_length=200, blank=True, null=True)
    link = models.URLField(blank=True, null=True)

class Blog(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(upload_to='picture of blog/', blank=True, null=True)
    tag = models.ManyToManyField(Tags, related_name="blog", blank=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class Contact(models.Model):
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    mail = models.CharField(max_length=30,blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)