from django.shortcuts import render

from .models import Gallery

def main(request):

    data = { 'admin_content': None }
    content_to_show = Gallery.objects.all()

    if content_to_show.exists():
        data['admin_content'] = content_to_show.order_by('date_created')
    
    return render(request, 'gallery.html', data)
