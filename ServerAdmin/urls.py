# -*- coding: utf-8 -*-
"""ServerAdmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.views.generic.base import RedirectView
#from material.frontend import urls as frontend_urls
from . import views




#urlpatterns = [
#        #url(r'^admin/', include(admin.site.urls)),
#        url(r'', include(frontend_urls)),
#        url(r'^account', views.index, name='index'),
#        url(r'^$', views.index, name='index'),
#    ]

urlpatterns = [
    #url(r'^$', admin.site.urls),
    #url('/', views.index, name='index'),
    url(r'^$', RedirectView.as_view(pattern_name='/admin', permanent=False)),
    url(r'^admin/', admin.site.urls),
]

admin.site.site_header = 'Server Control Panel'
admin.site.site_title = "Server Control Panel"
admin.site.site_url = '/admin'
admin.site.index_title = 'Server Control Panel'
#admin.empty_value_display = '**Empty**'
