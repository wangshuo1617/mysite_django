#-*-coding:utf-8-*-
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse(u'这是首页，应该展示最近的博客列表')

def detail(request):
    return HttpResponse(u'这是详情页，展示一篇博客的全部内容')

