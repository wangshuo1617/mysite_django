import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wxtj(request):
    return HttpResponse(u'weixin tongji ')
