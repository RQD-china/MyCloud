import imp
from django.views import View
from django.http import JsonResponse
from sympy import content
from app01.models import Comment, Articles
from django.db.models import F
from app01.utils.comment import find_root, find_root_sub

class CommentView(View):
    # 发布评论
    def post(self, request, nid):
        res = {
            'msg': '文章评论成功!',
            'code': 412,
            'self': None
        }
        # 登录校验
        if not request.user.username:
            res['msg'] = '请先登录再评论'
            return JsonResponse(res)
        
        # 评论内容校验
        data = request.data
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
    # 删除评论
    def delete(self, request, nid):
        res = {
            'msg': '评论删除成功!',
            'code': 412,
            'self': None
        }
        comment_query = Comment.objects.filter(nid=nid)
        comment_obj = comment_query.first()
        root_comment_obj = find_root(comment_obj)
        user = request.user
        
        # 判断删除权限
        if user == comment_obj.user or user.is_superuser:
            sub_list = []
            find_root_sub(comment_obj, sub_list)
                
            # 评论的回复数减少
            root_comment_obj.comment_count -= 1 + len(sub_list)
            root_comment_obj.save()
            
            # 文章评论数减少
            aid = comment_obj.article.nid
            Articles.objects.filter(nid=aid).update(
                comment_count=F('comment_count') - 1 - len(sub_list))
                
            # 删除评论
            comment_query.delete()
            res['code'] = 0
            return JsonResponse(res)
        res['msg'] = '用户验证失败'
        return JsonResponse(res)

class CommentDiggView(View):
    def post(self, request, nid):
        res = {
            'msg': '评论点赞成功!',
            'code': 412,
            'data': 0
        }

        # 登录校验
        if not request.user.username:
            res['msg'] = '请先登录再评论'
            return JsonResponse(res)
        
        #点赞+1
        comment_query = Comment.objects.filter(nid=nid)
        comment_query.update(digg_count=F('digg_count') + 1)
        res['code'] = 0
        res['data'] = comment_query.first().digg_count
        return JsonResponse(res)
