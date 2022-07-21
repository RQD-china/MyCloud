from django.views import View
from django.http import JsonResponse
from app01.models import Articles, Tags, Cover

class ArticleView(View):
    def post(self, request):
        res = {
            'data': '',
            'msg': '服务器内部错误，发布文章失败',
            'code': 412
        }

        data: dict = request.data
        extra = {**data}
        del extra['tags']
        article_obj = Articles.objects.create(**extra)
        if(article_obj):
            for tag in data['tags']:
                if not tag.isdigit():
                    tag = Tags.objects.create(title = tag)
                article_obj.tag.add(tag)    
            res['data'] = article_obj.nid
            res['msg'] = '文章发布成功！即将跳转...'
            res['code'] = 0
        return JsonResponse(res)