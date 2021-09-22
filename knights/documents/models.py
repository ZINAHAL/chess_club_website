from django.db import models

from django_better_admin_arrayfield.models.fields import ArrayField


MAX_LENGTH = 70

class DocumentsPageContent(models.Model):
    last_modified = models.DateField(auto_now=True)

    @property
    def policies(self):
        return self.policy_set.all()
    
    @property
    def forms(self):
        return self.form_set.all()
    
    def __str__(self):
        return f'Forms, Policies, Last Modified: {self.last_modified}'
    
        

class Policy(models.Model):
    document_name = models.CharField(max_length=MAX_LENGTH, null=True)
    file = models.FileField(null=True)
    display_page = models.ForeignKey(DocumentsPageContent, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return ''


class Form(models.Model):
    document_name = models.CharField(max_length=MAX_LENGTH)
    file = models.FileField(null=True)
    display_page = models.ForeignKey(DocumentsPageContent, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return ''
