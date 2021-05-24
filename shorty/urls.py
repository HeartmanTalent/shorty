from django.contrib import admin
from django.urls import path, re_path
from main.views import shorten, analysis, index, lengthen

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('shorten', shorten, name='shorten'),
    re_path(
        r'^(?P<slug>\w+)/$', lengthen, name='lengthen'),
    path('analysis', analysis, name='analysis')
]
