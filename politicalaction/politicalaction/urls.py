
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from cause import urls as cause_urls
from event import urls as event_urls
from politician import urls as politician_urls
from notification import urls as notification_urls

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^cause/', include(cause_urls)),

     url(r'^event/', include(event_urls)),

     url(r'^politician/', include(politician_urls)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
