from django.contrib import admin
from django.urls import path, include, re_path
from .views import index, pages

urlpatterns = [
    path('', index, name='index'),
    path('sunu-admin/', admin.site.urls, name='sunu-admin'),
    path('', include('authentification.urls')),

    # Matches any html file
    re_path(r'^.*\.*', pages, name='pages'),

]
