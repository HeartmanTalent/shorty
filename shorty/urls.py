from django.contrib import admin
from django.urls import path, re_path, include
from main.views import shorten, analysis, index, lengthen, delete, login
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analysis', analysis, name='analysis'),
    path("login/", login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('', index, name='index'),
    re_path(r'^delete/(?P<id>\d+)/$', delete, name='delete'),
    path('shorten', shorten, name='shorten'),
    re_path(
        r'^(?P<slug>\w+)/$', lengthen, name='lengthen'), #should always be at th bottom 

]
