from django import template
from app01.models import Articles, Cover, MenuImg
from app01.utils.search import Order
from django.utils.safestring import mark_safe

register = template.Library()

@register.inclusion_tag('my_tag/header.html')
def banner(menuName, article=None):
    img_obj = MenuImg.objects.all()
    img_list = [img.url.url for img in img_obj]
    if article:        
        cover = article.cover.url.url
        return {"img_list": [cover]}
    return {"img_list": img_list}

@register.simple_tag
def generate_order_html(request, key):
    # 获取参数
    query_params = request.GET.copy()
    order = ''
    order_list =[]
    
    # 创建排序与筛选实例
    if key == 'order':
        order = query_params.get(key)
        order_list=[('', '综合排序'),
                    ('-create_time', '最新发布'),
                    ('-look_count', '最多浏览'),
                    ('-digg_count', '最多点赞'),
                    ('-comment_count', '最多评论'),
                    ('-collects_count', '最多收藏')]
    elif key == 'word':
        order = query_params.getlist(key)
        order_list = [([''], '全部文章'),
                      (['0', '1000'], '百字短篇'),
                      (['1000', '10000'], '千字长文')]
    order_obj = Order(
        key=key,
        order=order,
        order_list=order_list,
        query_params=query_params
    )
    return mark_safe(order_obj.order_html())
