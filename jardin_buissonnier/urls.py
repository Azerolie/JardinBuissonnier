#-*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from blog import views
from accueil import views
from jardins import views
from contact import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^blog/', include('blog.urls')),
    url(r'^', include('accueil.urls')),
    url(r'^jardins/', include('jardins.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
