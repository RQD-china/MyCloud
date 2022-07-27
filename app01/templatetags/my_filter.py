from atexit import register
from django import template

# 注册
register = template.Library()

# 用户是否已经收藏文章
@register.filter
def is_collect(article, request):
    if str(request.user) == 'AnonymousUser':
        return ''
    if article in request.user.collects.all():
        return 'on'
    return ''
    
