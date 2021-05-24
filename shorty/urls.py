from django.contrib import admin
from django.urls import path, re_path
from main.views import shorten, analysis, index, lengthen, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    re_path(r'^delete/(?P<id>\d+)/$', delete, name='delete'),
    path('shorten', shorten, name='shorten'),
    re_path(
        r'^(?P<slug>\w+)/$', lengthen, name='lengthen'),
    path('analysis', analysis, name='analysis')
]
