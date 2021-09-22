from django.db import models

MAX_LENGTH = 254

class ContactUsContent(models.Model):
    number = models.CharField(max_length=MAX_LENGTH)
    email = models.EmailField(max_length=MAX_LENGTH)
    address = models.CharField(max_length=MAX_LENGTH)

    def __str__(self):
        return "phone, email, address"
    