from click import password_option
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.


def index(request):
    return HttpResponse("hello world!")


def uesr_list(request):
    return render(request, "user_list.html")


def tpl(request):
    name = "张三"
    userList = ["李四", "王五", "赵六"]
    userInfo = {"name": "陈睿", "salary": "114512", "role": "CEO"}
    infoList = [
        {"name": "陈睿", "salary": "114512", "role": "CEO"},
        {"name": "李旎", "salary": "114512", "role": "COO"}
    ]
    return render(request, "tpl.html", {"name": name, "list": userList, "info": userInfo, "infoList": infoList})


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    print(username)
    if username == 'admin' and password == '12345':
        return redirect("https://www.bilibili.com/")
    else:
        if username == 'admin':
            return render(request, "login.html", {"error": "密码错误"})
        else:
            return render(request, "login.html", {"error": "用户名不存在"})

from app.models import UserInfo

def orm(request):
    # UserInfo.objects.create(name = 'rqd', password = '123456', age = 18)
    UserInfo.objects.filter(name = 'rqd').delete()

    return HttpResponse("success")
