#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import string,urllib,urllib2,re,cookielib,datetime,json,hashlib

# Create your views here.
def md5(s):
    m=hashlib.md5()
    m.update(s)
    return m.hexdigest()

def user(request):
    #保存cookie的文件
    filename='cookie.txt'

    #获取cookie
    cookie=cookielib.MozillaCookieJar(filename)
    handler=urllib2.HTTPCookieProcessor(cookie)
    opener=urllib2.build_opener(handler)


    values = {'username':'3278663871@qq.com',
              'pwd':md5('5252mayi')}#向登录页面post的数据
    data=urllib.urlencode(values)#数据url编码
    headers={'Referer':'https://mp.weixin.qq.com/',
             'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
             'Connection': 'keep-alive',
             'Accept':'*/*',
             }#request header信息
    request=urllib2.Request('https://mp.weixin.qq.com/cgi-bin/login',data,headers)
    response=opener.open(request)#response内容，为一file对象实例
    cookie.save(ignore_discard=True, ignore_expires=True)#cookie保存
    #获取请求具体页面的token
    now=datetime.datetime.now()
    time=now.strftime('%Y%m%d %H%M%S')
    end_time=now.strftime('%Y-%m-%d')
    p1=re.compile(r'token=(.+)"')
    token_list=p1.findall(response.read())
    token=token_list[0]
    begin_date=raw_input('enter begin date:')
    data={'download':'1',
          'begin_date':'2016-02-01',
          'end_date':end_time,
          'source':'99999999',
          'token':token,
          'lang':'zh_CN',}
    url1='https://mp.weixin.qq.com/misc/useranalysis?&'+urllib.urlencode(data)
    con_req=urllib2.Request(url1)
    con_resp=opener.open(con_req).read()
    return HttpResponse(con_resp)
