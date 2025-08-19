from django.contrib import admin
from . models import Profile, Project_Tag, Project, Publications

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project_Tag)
admin.site.register(Project)
admin.site.register(Publications)