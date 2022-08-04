from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from api.views import login, article, comment, message

urlpatterns = [
    path('login/', login.LoginView.as_view()),  # 登录
    path('sign/', login.SignView.as_view()),    # 注册

    path('article/', article.ArticleView.as_view()),    # 发布文章
    path('message/', message.AddMessageView.as_view()),
    
    re_path('article/(?P<nid>\d+)/', article.ArticleView.as_view()),    # 编辑文章
    re_path('article/comment/(?P<nid>\d+)/', comment.CommentView.as_view()),    # 发布评论
    re_path('comment/digg/(?P<nid>\d+)/', comment.CommentDiggView.as_view()),    # 点赞评论
    re_path('article/digg/(?P<nid>\d+)/', comment.ArticleDiggView.as_view()),    # 点赞文章
    re_path('article/collect/(?P<nid>\d+)/', comment.ArticleCollectView.as_view()),    # 收藏文章
]
