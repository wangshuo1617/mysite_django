import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from django.shortcuts import render
from fangtan.models import duixiang,report
import string,re,jieba,jieba.analyse,pyglet,pytagcloud
from django.http import HttpResponse
from operator import itemgetter
# Create your views here.

def segf(content):
    out=jieba.cut(content,cut_all=False)
    nonsense=[]
    word_freq={}
    for x in out:
        if len(x)<2:
            continue
        elif x in nonsense:
            continue
        else:
            c=str(x)
            if x not in word_freq:
                word_freq[x]=1
            else:
                word_freq[x]+=1
    word_freq=sorted(word_freq.iteritems(), key=itemgetter(1), reverse=True)
    return word_freq


def all_duixiang(request):
    duixiang_list=duixiang.objects.all()
    context={'duixiang_list':duixiang_list,}

    return render(request,'fangtan/duixiang.html',context)

def report_list(request,duixiang_id):
    dx=duixiang.objects.get(pk=duixiang_id)
    report_list=dx.report_set.all()
    context={'report_list':report_list,}

    return render(request,'fangtan/report.html',context)

def report_detail(request,report_id):
    rep=report.objects.get(pk=report_id)
    content=rep.origin.read().replace('\n','<br>')
    fenxi=segf(content)
    string=' '
    for (k,v) in fenxi:
        string=string+k+' '+str(v)+'<br>'
    context={'content':content,
             'ctic':rep.ctic,
             'fenxi':string,}

    return render(request,'fangtan/report_detail.html',context)

def report_empty(request):
    return HttpResponse(u'<h1>No message</h1>')
    

    
    
