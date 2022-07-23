from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from api.views import login, article, comment

urlpatterns = [
    path('login/', login.LoginView.as_view()),  # 登录
    path('sign/', login.SignView.as_view()),    # 注册

    path('article/', article.ArticleView.as_view()),    # 发布文章
    re_path('article/(?P<nid>\d+)/', article.ArticleView.as_view()),    # 编辑文章
    re_path('article/comment/(?P<nid>\d+)/',
            comment.CommentView.as_view()),    # 发布评论
]
