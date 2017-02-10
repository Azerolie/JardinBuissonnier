#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('accueil.views',
    url(r'^$', 'page_accueil'),
)
