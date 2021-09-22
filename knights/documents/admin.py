from django.contrib import admin

from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from .models import DocumentsPageContent, Form, Policy
from knights.helper_classes import RemoveAddDeleteActions


class PolicyInline(admin.TabularInline):
    model = Policy
    extra = 1


class FormInline(admin.TabularInline):
    model = Form
    extra = 1


@admin.register(DocumentsPageContent)
class DocumentsPageAdmin(RemoveAddDeleteActions, admin.ModelAdmin, DynamicArrayMixin):
    inlines = [PolicyInline, FormInline]
