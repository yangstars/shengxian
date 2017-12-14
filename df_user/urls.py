# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_handle/$', views.register_handle),
    url(r'^login/$', views.login),
    url(r'^login_handle/$', views.login_handle),
    url(r'^register_exist/$', views.register_exist),
    url(r'^user_center_info/$', views.user_center_info),#个人信息
    url(r'^user_center_order/$', views.user_center_order),#全部订单
    url(r'^user_center_site/$', views.user_center_site),#收获地址
]
