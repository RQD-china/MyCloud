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
def generate_order_html(request):
    query_params = request.GET.copy()
    order = request.GET.get('order', '')
    order_obj = Order(
        order=order,
        order_list=[('-change_time', '综合排序'),
                    ('-create_time', '最新发布'),
                    ('-look_count', '最多浏览'),
                    ('-digg_count', '最多点赞'),
                    ('-comment_count', '最多评论'),
                    ('-collects_count', '最多收藏')],
        query_params=query_params
    )
    return mark_safe(order_obj.order_html())
