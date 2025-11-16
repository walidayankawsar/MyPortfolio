from django.contrib import admin
from . models import Profile, Tags, Project, Publications, Contact, Blog, skill, Education

# Register your models here.
admin.site.register(Profile)
admin.site.register(Tags)
admin.site.register(Project)
admin.site.register(Publications)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(skill)
admin.site.register(Education)