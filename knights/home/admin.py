from __future__ import unicode_literals
from django.contrib import admin

from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from .models import HomePageContent, Staff, Sponsor
from knights.helper_classes import RemoveAddDeleteActions


class StaffInline(admin.TabularInline):
    model = Staff
    extra = 1


class SponsorInline(admin.TabularInline):
    model = Sponsor
    extra = 1


@admin.register(HomePageContent)
class HomePageAdmin(RemoveAddDeleteActions, admin.ModelAdmin, DynamicArrayMixin):
    inlines = [StaffInline, SponsorInline]