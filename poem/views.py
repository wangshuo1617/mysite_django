#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse
import re,random

# Create your views here.
def random_poem(request):
    with open('result.txt','r') as f:
        con=f.readlines()#con：所有诗的列表
        ran=random.choice(con)#ran：某首诗
        rlist=re.split(r'【|】|；|,|）|，|。|？|！|：',ran)
        title=rlist[1]
        if '（' in rlist[2]:
            plist=rlist[3:]#plist的元素：一首诗中的某一行
        else:
            plist=rlist[2:]
        plist=[i.strip() for i in plist]
        for i in random.sample(range(len(plist)-1),1):#随机生成空缺句
            answer=plist[i].strip().decode('utf-8')
            plist[i]=' '#此时，plist保存了一首诗的各行和一个空行
        answerlist=[answer[i] for i in range(len(answer))]#answerlist保存正确句中各个单字
        miss=random.sample(''.join(plist).decode('utf-8'),12-len(answer))#补充到12个字
        guesslist=miss+answerlist#guesslist中共12个单字，其中包含answerlist的正确和miss中的补充
        random.shuffle(guesslist)#打乱顺序的guesslist
        context={'plist':plist,'title':title,
                 'answer':answer,'answerlist':answerlist,
                 'guesslist':guesslist,'indexlist':range(12),}
        return render(request,'poem/index.html',context)
        
def test(request):
    return render(request,'poem/test.html')
    
    
