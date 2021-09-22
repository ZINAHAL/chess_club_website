from django.conf.urls import url

from .views import main, createInformationPage

urlpatterns = [
    url(r'^$', main, name='calendar'),
    url(r'^(?P<event_id>[0-9]+)$', createInformationPage, name='eventInformation')
]