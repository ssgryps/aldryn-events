# -*- coding: utf-8 -*-

from aldryn_events.views import event_list, event_dates, event_list_archive, event_detail, reset_event_registration
from django.urls import path, re_path

urlpatterns = [
    path('', event_list, name='events_list'),
    path('get-dates/', event_dates, name='get-calendar-dates'),
    path('get-dates/<int:year>/<int:month>/', event_dates, name='get-calendar-dates'),
    re_path(r'^(?P<year>\d{4})/$', event_list, name='events_list-by-year'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', event_list, name='events_list-by-month'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', event_list, name='events_list-by-day'),
    path('archive/', event_list_archive, name='events_list_archive'),
    re_path(r'^archive/(?P<year>\d{4})/$', event_list_archive, name='events_list_archive-by-year'),
    re_path(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$', event_list_archive, name='events_list_archive-by-month'),
    re_path(r'^(?P<slug>[\w_-]+)/$', event_detail, name='events_detail'),
    re_path(r'^(?P<slug>[\w_-]+)/reset/$', reset_event_registration, name='events_registration_reset'),
]
