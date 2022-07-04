"""Techme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import static

<<<<<<< HEAD
# from django.views.static import serve
# from django.conf.urls import url
=======
from django.views.static import serve
from django.conf.urls import url
>>>>>>> 9aa0749d6844365e1818bc248e88dbc11bd41642


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Site.urls')),
    path('',include('Account.urls')),
<<<<<<< HEAD
    # url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
=======
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
>>>>>>> 9aa0749d6844365e1818bc248e88dbc11bd41642
]
