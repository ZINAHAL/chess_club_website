from django.shortcuts import render

from .models import DocumentsPageContent

#Return the documents.html page
def main(request):

    data = { 'admin_content': None }
    content_to_show = DocumentsPageContent.objects.all()

    if content_to_show.exists():
        data['admin_content'] = content_to_show[0]
    
    return render(request, 'documents.html', data)
