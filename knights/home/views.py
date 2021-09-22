from __future__ import unicode_literals
from django.shortcuts import render

from .models import HomePageContent

#Return the index.html page
def index(request):

    data = { 'admin_content': None }
    content_to_show = HomePageContent.objects.all()

    if content_to_show.exists():
        data['admin_content'] = content_to_show[0]

    return render(request, 'index.html', data)

