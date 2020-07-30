from django import forms
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ('phone' ,'email', 'linkedin', 'github')

class EducationForm(forms.ModelForm):
    class Meta:
        model = models.Education 
        fields = ('institute', 'passed', 'score')

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = models.Experience 
        fields = ('role', 'detail')

class SkillForm(forms.ModelForm):
    class Meta:
        model = models.Skill
        fields = ('skill', 'strength')