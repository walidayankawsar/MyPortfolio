from django.db import models

# Create your models here.
class Profile(models.Model):
    picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    graduate = models.CharField(max_length=100, blank=True, null=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    work = models.CharField(max_length=100, blank=True, null=True)
    work_experience = models.TextField(blank=True, null=True)
    work_date = models.DateField(blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True)
    education_description = models.TextField(blank=True, null=True)
    education_date = models.DateField(blank=True, null=True)

class Project_Tag(models.Model):
    Tag_name = models.CharField(max_length=100, unique=True, blank=True, null=True)

class Project(models.Model):
    project_name = models.CharField(max_length=100, blank=True, null=True)
    tags = models.ManyToManyField(Project_Tag, related_name="posts", blank=True, null=True)
    short_description = models.TextField(max_length=500,blank=True, null=True)
    ful_description = models.TextField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    website_link = models.URLField(blank=True, null=True)
