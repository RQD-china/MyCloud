import imp
from re import U
from click import password_option
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib import auth
from sympy import re
from app01.models import Articles, Tags, Cover

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

# 后台页面    
# 个人中心
def backend(request):
    if not request.user.username:
        return redirect('/')
    return render(request, 'backend/my_homepage.html', locals())

# 修改信息
def edit_info(request):
    if not request.user.username:
        return redirect('/')
    return render(request, 'backend/edit_info.html', locals())

# 修改密码
def reset_pwd(request):
    if not request.user.username:
        return redirect('/')
    return render(request, 'backend/reset_pwd.html', locals())

# 添加文章
def add_article(request):
    if not request.user.username:
        return redirect('/')
    # 获取标签列表
    tag_list = Tags.objects.all()
    # 获取封面列表
    cover_list = Cover.objects.all()
    cover_num = len(cover_list)
    print(cover_num)
    return render(request, 'backend/add_article.html', locals())

# 文章封面
def article_banner(request):
    if not request.user.username:
        return redirect('/')
    return render(request, 'backend/article_banner.html', locals())

# 头像列表
def avatar_list(request):
    if not request.user.username:
        return redirect('/')
    return render(request, 'backend/avatar_list.html', locals())


