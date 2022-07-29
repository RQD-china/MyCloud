import imp
import json
from re import U
from click import password_option
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib import auth
from django.db.models import F
from sympy import re
from app01.models import Articles, Tags, Cover
from app01.utils.comment import get_comment
from app01.utils.search import Order
import math

# Create your views here.

def change_type(byte):    
    if isinstance(byte, bytes):
        return str(byte,encoding="utf-8")  
    return json.JSONEncoder.default(byte)

# 主页
def index(request):
    if not request.GET:
        return redirect('/?page=1')
    
    article_list = Articles.objects.all().order_by('-change_date')
    recommend_list = Articles.objects.filter(recommend = True).order_by('-change_date')[:6]
    
    query_params = request.GET.copy()
    
    params = {
        'current_page': int(request.GET.get('page')),
        'base_url': request.path_info,
        'total': article_list.count(),
        'page_size': 2
    }
    if params['current_page'] > math.ceil(params['total'] / params['page_size']):
        return redirect('/?page=1')
    start = (params['current_page'] - 1) * params['page_size']
    article_list = article_list[start : start + params['page_size']]
    return render(request, 'index.html', locals())
    
# 文章
def article(request, nid):
    article_query =  Articles.objects.filter(nid = nid)
    if not article_query:
        return redirect('/')
    article_query.update(look_count=F('look_count') + 1)
    article = article_query.first()
    comment_list = get_comment(nid)
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

# 搜索页面
def search(request):
    # 获取url参数
    search_key = request.GET.get('key', '')
    order = request.GET.get('order', '')
    word = request.GET.getlist('word', '')
    page = int(request.GET.get('page', ''))
    query_params = request.GET.copy()
    
    # 获取页面数
    if not page:
        if not request.GET:
            return redirect(request.path_info + '?page=1')
        else:
            return redirect(request.get_full_path() + '&page=1')
    
    # 生成页面数据
    article_list = Articles.objects.filter(
        title__contains=search_key)
    params = {
        'current_page': page,
        'key': search_key,
        'base_url': request.path_info,
        'total': article_list.count(),
        'page_size': 4
    }

    # 排序/筛选
    if len(word) == 2:
        article_list = article_list.filter(word__range=word)

    if order:
        try:
            article_list = article_list.order_by(order)
        except Exception:
            pass
    
    # 分页
    if params['current_page'] > math.ceil(params['total'] / params['page_size']):
        params['current_page'] = 1
    start = (params['current_page'] - 1) * params['page_size']
    article_list = article_list[start: start + params['page_size']]
    
    # 返回页面
    return render(request, 'search.html', locals())

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
    return render(request, 'backend/add_article.html', locals())

# 编辑文章
def edit_article(request, nid):
    if not request.user.username:
        return redirect('/')
    # 获取标签列表
    tag_list = Tags.objects.all()
    # 获取封面列表
    cover_list = Cover.objects.all()
    # 获取文章信息
    article_obj = Articles.objects.get(nid = nid)
    article_content = article_obj.content
    article_title = article_obj.title
    article_author = article_obj.author
    article_source = article_obj.source
    article_cover_id = article_obj.cover_id
    article_recommend = article_obj.recommend
    article_abstract = article_obj.abstract
    article_tags = [str(tag.nid) for tag in article_obj.tag.all()]
    return render(request, 'backend/edit_article.html', locals())

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


