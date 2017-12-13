#-*- coding:utf-8 -*-
from django.shortcuts import render ,redirect
from models import *
from hashlib import sha1 #引入加密模块

# Create your views here.

#跳转注册页面
def register(request):
    return render(request,'df_user/register.html')


#跳转注册页面
def login(request):
    return render(request,'df_user/login.html')


def register_handle(request):
    post = request.POST
    uname = post.get("user_name")
    upwd = post.get("pwd")
    cpwd = post.get("cpwd")
    uemail = post.get("email")
    #判断两次密码是否一致
    if upwd != cpwd:
        return  redirect('/user/register')

    #密码加密
    s1 = sha1()
    s1.update(upwd)
    upwd2= s1.hexdigest()

    #创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd =upwd2
    user.uemail = uemail
    user.save()

    #跳转到登陆页面
    return redirect('/user/login')










