from django.db import models

class Contact(models.Model):
    email = models.EmailField(max_length=200)
    linkedin = models.URLField(max_length=200)
    github = models.URLField(max_length=200)
    phone = models.PositiveIntegerField()

    def __str__(self):
        return self.email

class Education(models.Model):
    institute = models.CharField(max_length=200)
    passed = models.DateField()
    score = models.CharField(max_length=100)
    email = models.ForeignKey(Contact, default=1, on_delete=models.SET_DEFAULT)
    def __str__(self):
        return self.institute

class Experience(models.Model):
    role = models.CharField(max_length=200)
    detail = models.TextField(max_length=1000)
    email = models.ForeignKey(Contact, default=1, on_delete=models.SET_DEFAULT)
    def __str__(self):
        return self.role

class Skill(models.Model):
    skill = models.CharField(max_length=200)
    strength = models.CharField(max_length=200)
    email = models.ForeignKey(Contact, default=1, on_delete=models.SET_DEFAULT)
    def __str__(self):
        return self.skill
    
