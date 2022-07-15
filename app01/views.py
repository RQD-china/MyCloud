import imp
from django.shortcuts import render
from django.http import JsonResponse
from django import forms
from django.contrib import auth

# Create your views here.

# 主页
def Index(request):
    return render(request, 'index.html')
    
# 新闻页
def News(request):
    return render(request, 'news.html')

# 登录表单验证
class LoginForm(forms.Form):
    name = forms.CharField(error_messages={'required': '请输入用户名'})
    pwd = forms.CharField(error_messages={'required': '请输入密码'})

    # 全局钩子
    def clean(self):
        name = self.cleaned_data.get('name')
        pwd = self.cleaned_data.get('pwd')

        user = auth.authenticate(username = name, password = pwd)

        if not user:
            self.add_error('pwd', '用户名或密码错误')
            return self.cleaned_data
        self.cleaned_data['user'] = user
        return self.cleaned_data

# 登录错误处理
def cleanForm(form):
    # 表单验证
    errorDict: dict = form.errors
    # 获取错误代码
    errorCode = len(list(errorDict.keys()))
    # 拿到第一个错误信息字段名
    errorValid = list(errorDict.keys())[0]
    # 获取第一个错误信息
    errorMsg = errorDict[errorValid][0]

    return errorCode, errorMsg, errorValid

# 登录页面
def Login(request):
    if request.method == 'POST':
        res = {
            'code': 0,
            'msg': "登录成功",
            'self': None
        }
        print(11)
        form = LoginForm(request.data)

        # 登录失败
        if not form.is_valid():
            res['code'], res['msg'], res['self'] = cleanForm(form)
            return JsonResponse(res)
        
        # 登录成功
        user = form.cleaned_data.get('user')
        auth.login(request, user)
        return JsonResponse(res)
    return render(request, 'login.html')
    
# 注册页面
def Sign(request):
    return render(request, 'sign.html')