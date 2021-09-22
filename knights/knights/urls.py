from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from home import urls as home_urls
from accounts import urls as accounts_urls
from documents import urls as documents_urls
from club_calendar import urls as calendar_urls
from contact_us import urls as contact_urls
from gallery import urls as gellery_urls
from gallery.admin import gallery_admin_site

admin.site.site_header = "Knights of Éanna"
admin.site.site_title = "Knights of Éanna"
admin.site.index_title = "Welcome to The Club's Admin Site!"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^887766/', gallery_admin_site.urls),
    url(r'^', include(home_urls)),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^documents/', include(documents_urls)),
    url(r'^calendar/', include(calendar_urls)),
    url(r'^contact/', include(contact_urls)),
    url(r'^gallery/', include(gellery_urls))
]

# By default the django development server doesn't serve media files, only static ones, so the below is needed to do that
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )
