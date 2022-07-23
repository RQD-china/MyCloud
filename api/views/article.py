from django.views import View
from django.http import JsonResponse
from app01.models import Articles, Tags, Cover
from app01.views import article

# 给文章添加标签
def add_tags(tags, article_obj):
    for tag in tags:
        if not tag.isdigit():
            tag = Tags.objects.create(title = tag)
        article_obj.tag.add(tag)

# 文章相关请求
class ArticleView(View):
    # 添加文章
    def post(self, request):
        res = {
            'data': '',
            'msg': '服务器内部错误，发布文章失败',
            'code': 412
        }

        # 更新数据
        extra = {**request.data}
        tags = extra['tags']
        del extra['tags']
        article_obj = Articles.objects.create(**extra)
        
        # 更新标签
        if(article_obj):
            add_tags(tags, article_obj)
            
            # 返回成功
            res['data'] = article_obj.nid
            res['msg'] = '文章发布成功！即将跳转...'
            res['code'] = 0
        return JsonResponse(res)

    # 编辑文章
    def put(self, request, nid):
        res = {
            'msg': '编辑的文章不存在！',
            'code': 404
        }        
        article_query = Articles.objects.filter(nid = nid)
        if not article_query:
            return JsonResponse(res)
        
        # 更新数据
        extra = {**request.data}
        tags = extra['tags']
        del extra['tags']
        article_query.update(**extra)
        
        # 更新标签
        article_obj = article_query.first()
        article_obj.tag.clear()
        add_tags(tags, article_obj)
        
        # 返回成功
        res['msg'] = '文章发布成功！即将跳转...'
        res['code'] = 0
        return JsonResponse(res)
    