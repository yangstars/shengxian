# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns=[
        url(r'^register/$',views.register),
        url(r'^register_handle/$',views.register_handle),
        url(r'^login/$',views.login),
        url(r'^login_handle/$',views.login_handle),
        url(r'^userinfo/$',views.userInfo),
        url(r'^register_exist/$', views.register_exist)

]