from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request, 'index.html')
    
def News(request):
    return render(request, 'news.html')

def Login(request):
    return render(request, 'login.html')
    
def Sign(request):
    return render(request, 'sign.html')