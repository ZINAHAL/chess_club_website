from django.conf.urls import url

from .views import contactPageMain

urlpatterns = [
    url(r'^$', contactPageMain, name='contactUs')
] 