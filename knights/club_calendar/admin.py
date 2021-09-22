from django.contrib import admin

from .models import Event, Section

class SectionInline(admin.StackedInline):
    model = Section
    extra = 1

@admin.register(Event)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'location']
    inlines = [ SectionInline ]