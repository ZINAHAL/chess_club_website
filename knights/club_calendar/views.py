from django.shortcuts import render

from .models import Event

def main(request):

    data = { 'admin_content': None }
    content_to_show = Event.objects.all()

    if content_to_show.exists():
        data['admin_content'] = content_to_show.order_by('date')

    return render(request, 'calendar.html', data)


def createInformationPage(request, event_id):
    event_info = Event.objects.get(id=event_id)
    return render(request, 'event_information.html', {'event' : event_info})