from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from tours.views import pageNotFound, ServerError

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tours.urls'))
]

handler404 = pageNotFound
handler500 = ServerError

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
