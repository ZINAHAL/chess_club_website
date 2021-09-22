from django.db import models

from ckeditor.fields import RichTextField

MAX_LENGTH = 200

class Gallery(models.Model):
    title = models.CharField(max_length=MAX_LENGTH)
    description = RichTextField(blank=True)
    date_created = models.DateField(auto_now_add=True)

    @property
    def gallery_photoes(self):
        return self.photograph_set.all()

    def __str__(self):
        return self.title
    
class Photograph(models.Model):
    image = models.ImageField()
    description = models.TextField(blank=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    def __str__(self):
        return ''
    
    