# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
import df_user.views as df_user

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^goods/',include('df_goods.urls')),
    url(r'^user/',include('df_user.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
]
