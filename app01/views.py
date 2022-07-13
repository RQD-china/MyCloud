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
        data = request.data
        print(data)
        return JsonResponse(data)
    return render(request, 'login.html')
    
def Sign(request):
    return render(request, 'sign.html')