import imp
from re import U
from click import password_option
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib import auth

# Create your views here.

# 主页
def index(request):
    return render(request, 'index.html', {'request': request})
    
# 新闻页
def news(request):
    return render(request, 'news.html')

# 登录页面
def login(request):
    return render(request, 'login.html')

# 注册页面
def sign(request):
    return render(request, 'sign.html')

# 注销
def logout(request):
    auth.logout(request)
    return redirect('/')
