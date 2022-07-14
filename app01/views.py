from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

def Index(request):
    return render(request, 'index.html')
    
def News(request):
    return render(request, 'news.html')

def Login(request):
    if request.method == 'POST':
        res = {
            'code': 0,
            'msg': "登录成功",
            'self': None
        }
        data = request.data
        name = data['username']
        pwd = data['password']
        if not name:
            res['code'] = 1
            res['msg'] = '请输入用户名'
            res['self'] = 'name'
            return JsonResponse(res)
        if not pwd:
            res['code'] = 2
            res['msg'] = '请输入密码'
            res['self'] = 'pwd'
            return JsonResponse(res)

        if name != 'admin' or pwd != '12345':
            res['code'] = 3
            res['msg'] = '用户名或密码错误'
            res['self'] = 'pwd'
            return JsonResponse(res)
        return JsonResponse(res)
    return render(request, 'login.html')
    
def Sign(request):
    return render(request, 'sign.html')