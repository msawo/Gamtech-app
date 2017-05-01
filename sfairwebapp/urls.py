"""sfairwebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^suggest/$', views.suggestion_view, name='suggestion'),
    url(r'^suggestion_passed/$',
        TemplateView.as_view(template_name='suggestion_passed.html'),
        name='suggestion_passed'),
    url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^$', views.home_page, name='home'),
    url(r'^courses/', include('collection.urls', namespace='courses')),
]

urlpatterns += staticfiles_urlpatterns()
