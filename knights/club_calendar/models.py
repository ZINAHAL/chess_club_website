from django.db import models

from ckeditor.fields import RichTextField

MAX_LENGTH = 100
URL_HELP_TEXT = '''This field is optional. Fill this field only if the event is external ie organized by another organization, 
                    and a url is available. If the event is internal ie organized by the club, then please fill out the below 
                    form to create a dedicated webpage for the event within the website.'''

class Event(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    date = models.DateField()
    location = models.CharField(max_length=MAX_LENGTH)
    information_url = models.URLField(blank=True, help_text=URL_HELP_TEXT)

    @property
    def informationSections(self):
        return self.section_set.all().order_by('id')
    
    def __str__(self):
        return self.name


class Section(models.Model):
    title = models.CharField(max_length=MAX_LENGTH)
    paragraph = RichTextField() 
    # image = models.ImageField(blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return ''
    
