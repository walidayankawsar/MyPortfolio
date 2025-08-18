from django.db import models

# Create your models here.
class Profile(models.Model):
    picture = models.ImageField(upload_to='profile/')
    graduate = models.CharField(max_length=100)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    description = models.TextField()
    work = models.CharField(max_length=100)
    work_experience = models.TextField()
    work_date = models.DateField()
    education = models.CharField(max_length=100)
    education_description = models.TextField()
    education_date = models.DateField()

class Project_Tag(models.Model):
    Tag_name = models.CharField(max_length=100)

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    tags = models.ManyToManyField(Project_Tag, related_name="posts")
    description = models.TextField()
    github_link = models.URLField()
    website_link = models.URLField()
