import imp
from re import U
from click import password_option
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib import auth
from sympy import re
from app01.models import Articles

# Create your views here.

# 主页
def index(request):
    return render(request, 'index.html', {'request': request})
    
# 文章
def article(request, nid):
    article_query =  Articles.objects.filter(nid = nid)
    if not article_query:
        return redirect('/')
    article = article_query.first()
    return render(request, 'article.html', locals())

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
