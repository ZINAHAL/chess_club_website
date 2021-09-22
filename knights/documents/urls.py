from .views import main
from django.conf.urls import url

urlpatterns = [
    url(r'^$', main, name='documents')
]