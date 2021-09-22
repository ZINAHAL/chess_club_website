from django.contrib import admin

from .models import ContactUsContent
from knights.helper_classes import RemoveAddDeleteActions

@admin.register(ContactUsContent)
class ContactUsAdmin(RemoveAddDeleteActions, admin.ModelAdmin):
    list_display = ['email', 'number', 'address']
