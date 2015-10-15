from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'API.views.home'),
    url(r'^mynetaapi', 'API.views.mynetaapi'),
)
