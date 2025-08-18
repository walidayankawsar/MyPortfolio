from django.contrib import admin
from . models import Profile, Tag, Project

# Register your models here.
admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Project)