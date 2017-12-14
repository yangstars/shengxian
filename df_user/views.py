# -*- coding: utf-8 -*-
from django.shortcuts import render ,redirect
from models import *
from hashlib import sha1 #引入加密模块
from django.http import JsonResponse
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request,'df_user/index.html')

#跳转注册页面
def register(request):
    return render(request,'df_user/register.html')


#跳转登陆页面
def login(request):
    #如果cookie中有用户名的话，直接取出来进行显示
    uname = request.COOKIES.get('uname','')
    context={'title':'用户登陆','error_name':0,'error_upwd':0,'uname':uname}
    return render(request,'df_user/login.html',context)


def userInfo(request):
    return render(request,'df_user/user_center_info.html')


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

def login_handle(request):
    post = request.POST
    uname = post.get("username")
    jizhu = post.get("jizhu",0)
    #密码加密
    upwd = post.get("pwd")
    #根据uname 查询数据库
    #obj=UserInfo.objects.filter(uname=name,upwd=pwd2).first()
    user = UserInfo.objects.filter(uname=uname)
    #判断用户是否存在
    if len(user) ==1:
        s1 = sha1()
        s1.update(upwd)
        upwd2 = s1.hexdigest()
        if upwd2 == user[0].upwd:
            response =  HttpResponseRedirect('/user/userinfo')
            #记住密码 ,保存cookie 和session
            if jizhu == 1:
                response.set_cookie('uname', uname)
            else:
                response.set_cookie('uname','',max_age=-1)
            request.session['user_id_']=user[0].id
            request.session['user_name']=user[0].uname

            #登陆成功，保存cookie，跳转页面
            # 1、生成随机字符串（sessionID）
            # 2、通过cookie发送给客户端
            # 3、服务端保存{zhanggen随机字符串:{'name':'zhanggen'.'email':'zhanggen@le.com'}}
            # request.session['uname'] = user[0].uname
            # request.session['uemail'] = user[0].uemail
            print "login success!"
            return response
        else:
            context = {'title':'用户登陆','error_name':'0','error_pwd':'1','uname':uname,'upwd':upwd}
            return render(request,'df_user/login.html/',context)

    else:
        context={'title':'用户登陆','error_name':'1','error_pwd':'0','uname':uname,'upwd':upwd}
        return render(request,'df_user/login.html/',context)


def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})














