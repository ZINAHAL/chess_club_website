from __future__ import unicode_literals
from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField
from ckeditor.fields import RichTextField


MAX_LENGTH = 70

class HomePageContent(models.Model):
    summary_introduction = RichTextField()
    summary_image = models.ImageField(null=True)
    benefactors = ArrayField(models.CharField(max_length=MAX_LENGTH), null=True)

    @property
    def committee(self):
        return self.staff_set.filter(group__exact='0')
    
    @property
    def coaches(self):
        return self.staff_set.filter(group__exact='1')

    @property
    def sponsors(self):
        return self.sponsor_set.all()
    
    def __str__(self):
        return "Home"
    

class Staff(models.Model):
    GROUP_CHOICES = [ ('0', 'Committee'), ('1', 'Coaches') ]
    fullname = models.CharField(max_length=MAX_LENGTH)
    group = models.CharField(max_length=1, choices=GROUP_CHOICES)
    position = models.CharField(max_length=MAX_LENGTH)
    image = models.ImageField(null=True)
    display_page = models.ForeignKey(HomePageContent, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.fullname


class Sponsor(models.Model):
    company_name = models.CharField(max_length=MAX_LENGTH)
    company_logo = models.ImageField(null=True)
    company_homepage_URL = models.URLField()
    display_page = models.ForeignKey(HomePageContent, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.company_name
