from django.shortcuts import render
from django.http import JsonResponse
from django import forms
from django.urls import is_valid_path

# Create your views here.

def Index(request):
    return render(request, 'index.html')
    
def News(request):
    return render(request, 'news.html')

class LoginForm(forms.Form):
    name = forms.CharField(error_messages={'required': '请输入用户名'})
    pwd = forms.CharField(error_messages={'required': '请输入密码'})

def Login(request):
    if request.method == 'POST':
        res = {
            'code': 0,
            'msg': "登录成功",
            'self': None
        }
        data = request.data
        form = LoginForm(data)

        if not form.is_valid():
            # 表单验证
            errorDict = form.errors

            # 拿到第一个错误信息字段名
            errorValid = list(errorDict.keys())[0]
            print(errorValid)
            
            # 获取第一个错误信息
            errorMsg = errorDict[errorValid][0]
            res['code'] = len(list(errorDict.keys()))
            res['msg'] = errorMsg
            res['self'] = errorValid
            return JsonResponse(res)
        name = data['name']
        pwd = data['pwd']
        if name != 'admin' or pwd != '12345':
            res['code'] = 3
            res['msg'] = '用户名或密码错误'
            res['self'] = 'pwd'
            return JsonResponse(res)
        return JsonResponse(res)
    return render(request, 'login.html')
    
def Sign(request):
    return render(request, 'sign.html')