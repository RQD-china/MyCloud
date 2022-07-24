import imp
from django.views import View
from django.http import JsonResponse
from sympy import content
from app01.models import Comment, Articles
from django.db.models import F
from app01.utils.comment import find_root

class CommentView(View):
    # 发布评论
    def post(self, request, nid):
        res = {
            'msg': '文章评论成功!',
            'code': 412,
            'self': None
        }
        # 评论内容校验
        data = request.data
        if not request.user.username:
            res['msg'] = '请先登录再评论'
            return JsonResponse(res)
        content = data.get('content')
        if not content:
            res['msg'] = '请输入评论内容'
            res['self'] = 'content_textarea'
            return JsonResponse(res)
        
        # 添加评论数据
        cid = data.get('cid')
        if cid:
            comment_obj = Comment.objects.create(
                content=content,
                user=request.user,
                article_id=nid,
                parent_comment_id=cid
            )
            root_comment_obj = find_root(comment_obj)
            root_comment_obj.comment_count += 1
            root_comment_obj.save()
        else:
            Comment.objects.create(
                content=content,
                user=request.user,
                article_id=nid
            )
        res['code'] = 0

        # 文章评论数更新
        Articles.objects.filter(nid=nid).update(
            comment_count=F('comment_count') + 1)
        return JsonResponse(res)
