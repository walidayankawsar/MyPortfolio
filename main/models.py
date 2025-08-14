from django.db import models

# Create your models here.
class Profile(models.Model):
    picture = models.ImageField(upload_to='profile/')
    graduate = models.CharField(max_length=100)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    description = models.TextField(max_length=1000)
    work = models.CharField(max_length=100)
    work_experience = models.TextField(max_length=500)
    work_date = models.DateField()
    education = models.CharField(max_length=100)
    education_description = models.TextField(max_length=500)
    education_date = models.DateField()