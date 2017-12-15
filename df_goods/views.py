# -*- coding: utf-8 -*-
from django.shortcuts import render ,redirect
from models import *
from hashlib import sha1 #引入加密模块
from django.http import JsonResponse
from django.http import HttpResponseRedirect
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#跳转注册页面
def index(request):
    return render(request,'df_goods/index.html')