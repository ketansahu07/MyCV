from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact, Education, Experience, Skill
from . import forms
from django.contrib.auth.decorators import login_required

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

@login_required(login_url="/accounts/login/")
def create_cv(request):
    if request.method == 'POST':
        ConForm = forms.ContactForm(request.POST)
        EduForm = forms.EducationForm(request.POST)
        ExpForm = forms.ExperienceForm(request.POST)
        SkForm = forms.SkillForm(request.POST)
        if ConForm.is_valid() and EduForm.is_valid() and ExpForm.is_valid() and SkForm.is_valid():
            instance1 = ConForm.save(commit=False)
            instance2 = EduForm.save(commit=False)
            instance3 = ExpForm.save(commit=False)
            instance4 = SkForm.save(commit=False)
            instance1.user = request.user
            instance2.user = request.user
            instance3.user = request.user
            instance4.user = request.user
            instance1.save()
            instance2.save()
            instance3.save()
            instance4.save()
            return redirect('main:profile')
    else:
        ConForm = forms.ContactForm()
        EduForm = forms.EducationForm()
        ExpForm = forms.ExperienceForm()
        SkForm = forms.SkillForm()
    return render(request, 'main/create_cv.html', {'Cform':ConForm, 'Edform':EduForm, 'Exform':ExpForm, 'Sform':SkForm})