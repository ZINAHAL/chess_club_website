from django.contrib import admin

from .models import Gallery, Photograph

class GalleryAdmin(admin.AdminSite):
    site_header = 'Independent Admin Site for Gallery'

gallery_admin_site = GalleryAdmin(name='gal765leryxxx')

# -------- The above creates admin site that is independent of the main admin site -------- 

class PhotographInLine(admin.TabularInline):
    model = Photograph
    extra = 1

class GalleryPageAdmin(admin.ModelAdmin):
    inlines = [PhotographInLine]

gallery_admin_site.register(Gallery, GalleryPageAdmin)

    

