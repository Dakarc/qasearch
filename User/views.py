# _*_ coding: utf-8 _*_
# 记得安装OpenSSL
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import TddsQuestions
from .models import Searchlog

import requests
import json
import time,datetime
import urllib3
from urllib import parse

import logging              # 日志

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logger = logging.getLogger('log')   #设置日志类型

# Create your views here.

# def hello(request):
#     context          = {}
#     context['hello'] = 'Hello World!'
#     return render(request, 'hello.html', context)

#首页
def index(request):
    return render(request=request, template_name='User/index.html')

# 输入问题
def theinput(request):
    return render(request, template_name='User/theinput.html')

#接收问题
def search(request):

    # 1.接收问题

    question = request.POST.get('question')
    page = request.POST.get('page') if (request.POST.get('page')) else 0

    # 保存搜索的问题到MySQL
    #查询问题搜索记录是否存在,存在就次数加一,不创建新的数据;不存在就创建记为1
    """
    logInfo = Searchlog.objects.get(content = question)
    if logInfo:
        # 次数加一
        logInfo.num =logInfo.num + 1
        logInfo.save()
        #TODO:这里查询布道会报错
    else:
        #创建一条
        searchlog = Searchlog()
        searchlog.content = question
        searchlog.num = 1
        searchlog.ip = '100.102.103.11'
        searchlog.ss_time = "2019:07:02 17:35:01"
        searchlog.save()

    time_now = time.time()
    logger.info('开始执行search！ 开始时间:{};问题:{};页码:{}'.format(datetime.datetime.now(),question,page))
    """
    time_now = time.time()

    # 2.搜索问题
    # url = "https://api.askmimei.com/tls/liaobei/liaoBeiSearch.do" #原来的地址
    url = "https://pro.tuodandashi.com/liaobei/searchLiaoBei"

    # q = parse.urlencode({'q':question,'page':page})
    q = parse.urlencode({'key':question,'pageNo':page,'pageSize':10})

    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "PostmanRuntime/7.15.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "bc229a34-14cf-4422-8f1b-c07e14b6b925,ba5724e2-3a2f-48aa-a0be-5c942fad3012",
        'Host': "api.askmimei.com",
        'accept-encoding': "gzip, deflate",
        'content-length': "27",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=q, headers=headers,verify=False)

    print(response)
    print(type(response))

    # logger.info('得到返回结果response！ 得到时间:{};消耗时间:{};信息内容:{}'.format(datetime.datetime.now(),time.time()-time_now,json.loads(response.text)))
    logger.info('得到返回结果response！ 得到时间:{};消耗时间:{}'.format(datetime.datetime.now(),time.time()-time_now))

    text = json.loads(response.text)

    return render(request, 'User/answer_list.html', {'qas': text,'orig':json.dumps(question)})

# ajax接口
def search_port(request):

    # 1.ajax接收问题
    question = request.POST.get('question')
    page = request.POST.get('page') if (request.POST.get('page')) else 0

    time_now = time.time()
    logger.info('ajax开始执行search！ 开始时间:{};问题: {};页码: {}'.format(datetime.datetime.now(),question,page))

    # 2.搜索问题
    url = "https://api.askmimei.com/tls/liaobei/liaoBeiSearch.do"

    q = parse.urlencode({'q': question, 'page': page})

    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "PostmanRuntime/7.15.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "bc229a34-14cf-4422-8f1b-c07e14b6b925,ba5724e2-3a2f-48aa-a0be-5c942fad3012",
        'Host': "api.askmimei.com",
        'accept-encoding': "gzip, deflate",
        'content-length': "27",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=q, headers=headers, verify=False)

    logger.info('ajax得到返回结果response！ 得到时间:{};消耗时间:{}'.format(datetime.datetime.now(), time.time() - time_now))

    str = response.text
    arr = json.loads(str)
    arr['orig'] = question
    newstr = json.dumps(arr)


    # dict = json.load(response.text)
    # logger.info('转为字典的结果类型:{}'.format(type(dict)))
    # dict['orig'] = question

    # str = json.dump(dict)

    # logger.info('ajax返回数据类型:{}'.format(type(response.text)))

    # return HttpResponse(response.text, content_type='application/json')
    return HttpResponse(newstr, content_type='application/json')

#测试
# Get an instance of a logger
# logger = logging.getLogger(__name__)
def test(request):
    # return HttpResponse(222)
    return render(request, 'User/test.html')

def log_demo(request):
    # return render(request=request, template_name='User/test.html')
    # return HttpResponse(222)
    logger.info('请求成功！ response_code:{}；response_headers:{}；response_body:{}'.format('response_code', 'response_headers','response_body'[:251]))

    logger.error('请求出错：{}'.format('错误信息error111'))
    return HttpResponse(222)

def login(request):
    return  render(request,'User/login.html')

def login_check(request):
    # print(type(request.Post))
    # return HttpResponse('ok')
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'smart' and password == '123':
        return redirect('/')
    else:
        return redirect('/login')



def question(request):
    """问题输入"""
    return render(request, template_name='User/theinput.html')

def search_answer(request):
    """问题输入"""
    return render(request, template_name='User/theinput.html')

def ajax_test(request):
    '''显示ajax页面'''
    return render(request,'User/ajax_test.html')

def ajax_handle(request):
    '''显示ajax页面'''
    return JsonResponse({'res':1})

def login_ajax(request):
    '''ajax登录'''
    return render(request,'User/login_ajax.html')

def login_ajax_check(request):
    '''ajax登录验证'''
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'smart' and password == '123':
        return JsonResponse({'res':1})
    else:
        return JsonResponse({'res':0})

def chuancan(request):
    return render(request,'User/chuancan.html',{'content':'hello,world!','list':list(range(1,10))})

def show_ques(request):
    # 1.获取数据
    quess = TddsQuestions.objects.all()
    # 2.使用模板
    return render(request,'User/show_ques.html',{'quess':quess})

def detail(request,bid):
    # 1.查询问题的信息
    ques = TddsQuestions.objects.get(id=bid)
    # 2.查询相关答案的信息
    answs = ques.tddsanswers_set.all()  #这里都要小写
    # 3.使用模板
    return render(request,'User/detail.html',{'ques':ques,'answs':answs})