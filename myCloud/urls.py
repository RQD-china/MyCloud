"""myCloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from app01 import views

urlpatterns = [
    path('', views.index),
    path('news/', views.news),
    path('message/', views.message),
    path('login/', views.login),
    path('logout/', views.logout),
    path('sign/', views.sign),
    path('search/', views.search),
    path('admin/', admin.site.urls),
    
    path('backend/', views.backend),
    path('backend/edit_info/', views.edit_info),
    path('backend/reset_pwd/', views.reset_pwd),
    path('backend/add_article/', views.add_article),
    path('backend/article_banner/', views.article_banner),
    path('backend/avatar_list/', views.avatar_list),

    # 路由分发
    re_path(r'backend/edit_article/(?P<nid>\d+)/', views.edit_article),
    re_path(r'^article/(?P<nid>\d+)/', views.article),
    re_path(r'article_img/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^api/', include('api.urls')),
]
