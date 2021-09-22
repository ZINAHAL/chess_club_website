from django.shortcuts import render

from .models import ContactUsContent

def contactPageMain(request):
    data = { 'admin_content': None }
    content_to_show = ContactUsContent.objects.all()

    if content_to_show.exists():
        data['admin_content'] = content_to_show[0]

    return render(request, 'contact.html', data)
