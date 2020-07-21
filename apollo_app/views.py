from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('这是首页')

def login(request):
    return HttpResponse('这是登录')

def safe_a(request):
    return HttpResponse('实现A等级的安全级别')



def safe_b(request):
    return HttpResponse('实现B安全等级级别')