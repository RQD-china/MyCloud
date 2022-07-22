from django import template
from app01.models import Articles, Cover, MenuImg

register = template.Library()

@register.inclusion_tag('my_tag/header.html')
def banner(menuName, article=None):
    img_obj = MenuImg.objects.all()
    img_list = [img.url.url for img in img_obj]
    if article:        
        cover = article.cover.url.url
        print(cover)
        return {"img_list": [cover]}
    print(img_list)
    return {"img_list": img_list}