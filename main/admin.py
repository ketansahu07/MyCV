from django.contrib import admin

from .models import Contact, Education, Experience, Skill

admin.site.register(Contact)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
