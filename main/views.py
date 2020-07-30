from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact, Education, Experience, Skill

def home(request):
    return render(request, 'main/home.html')

def profile(request):
    con = Contact.objects.all()
    edu = Education.objects.all()
    exp = Experience.objects.all()
    skill = Skill.objects.all()
    return render(request,
                  'main/profile.html',
                  {'con':con, 'edu':edu, 'exp':exp, 'skill':skill})