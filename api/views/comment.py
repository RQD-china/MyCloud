import imp
from django.views import View
from django.http import JsonResponse
from sympy import content
from app01.models import Comment

class CommentView(View):
    # 发布评论
    def post(self, request, nid):
        res = {
            'msg': '文章评论成功!',
            'code': 412,
            'self': None
        }
        data = request.data
        if not request.user.username:
            res['msg'] = '请先登录再评论'
            return JsonResponse(res)
        content = data['content']
        if not content:
            res['msg'] = '请输入评论内容'
            res['self'] = 'content_textarea'
            return JsonResponse(res)

        Comment.objects.create(
            content=content,
            user=request.user,
            article_id=nid
        )
        res['code'] = 0
        return JsonResponse(res)
