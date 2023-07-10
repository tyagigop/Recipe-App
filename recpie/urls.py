
from django.contrib import admin
from django.urls import path
from home.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',home,name='home'),
    path('delete-rec/<id>/', delete_rec,name='delete_rec'),
    path('update-rec/<id>/', update_rec,name='update_rec'),

    path("admin/", admin.site.urls),
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                                document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
