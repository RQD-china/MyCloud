from django import template

register = template.Library()

@register.inclusion_tag('myTag/header.html')
def banner(menuName):
    imgList = [
        "https://pic.rmb.bdstatic.com/29cef03b42c2582c3ca4083b17c740f2.jpeg",
        "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farticle%2F029e7b8939f5af69c15c050123414a83911f12bb.jpg&refer=http%3A%2F%2Fi0.hdslb.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto",
        "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farchive%2Fef420937404e82282a8dd35db0a769ca8999c2fc.jpg&refer=http%3A%2F%2Fi0.hdslb.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto",
        "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farticle%2F457cc1e8cdad777d5b6eb0ea660dbed12c19a8ab.jpg&refer=http%3A%2F%2Fi0.hdslb.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto"
    ]
    return {"imgList": imgList}