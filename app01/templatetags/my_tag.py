import marshal
from ntpath import join
from unittest.mock import _patch_dict
from django import template
from app01.models import Tags, MenuImg
from app01.utils.search import Order
from django.utils.safestring import mark_safe

register = template.Library()

# 获取轮播图
@register.inclusion_tag('my_tag/header.html')
def banner(menuName, article=None):
    img_obj = MenuImg.objects.all()
    img_list = [img.url.url for img in img_obj]
    if article:        
        cover = article.cover.url.url
        return {"img_list": [cover]}
    return {"img_list": img_list}

# 获取排序/筛选标签
@register.simple_tag
def generate_order_html(request, key):
    # 获取参数
    query_params = request.GET.copy()
    order = query_params.get(key, '')
    order_list =[]
    
    # 创建排序与筛选实例
    if key == 'order':
        order_list=[('', '综合排序'),
                    ('-create_time', '最新发布'),
                    ('-look_count', '最多浏览'),
                    ('-digg_count', '最多点赞'),
                    ('-comment_count', '最多评论'),
                    ('-collects_count', '最多收藏')]
    elif key == 'word':
        order = query_params.getlist(key, [''])
        order_list = [([''], '全部文章'),
                      (['0', '1000'], '百字短篇'),
                      (['1000', '10000'], '千字长文')]
    elif key == 'tag':
        tag_list = Tags.objects.exclude(articles__isnull=True)
        order_list.append(('', '全部标签'))
        for tag in tag_list:
            order_list.append((tag.title, tag.title))
            
    order_obj = Order(
        key=key,
        order=order,
        order_list=order_list,
        query_params=query_params
    )
    return mark_safe(order_obj.order_html())

# 获取导航栏tab
@register.simple_tag
def dynamic_nav(request):
    path = request.path_info
    path_dict = {
        '/': '首页',
        '/news/': '新闻',
        '/message/': '留言板',
        '/about/': '关于',
        '/sites/': '导航',
    }
    nav_list = []
    for k, v in path_dict.items():
        if k == path:
            nav_list.append(f'<a href="{k}" class="active">{v}</a>')
            continue
        nav_list.append(f'<a href="{k}">{v}</a>')
    return mark_safe(''.join(nav_list))
