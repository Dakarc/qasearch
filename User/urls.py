from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'User'   # 这里是为了url反向解析用

urlpatterns = [
    # 这里放映射的view
    url(r'^$', views.index),                # 首页
    url(r'^theinput$', views.theinput),    # 输入问题_子页面
    url(r'^search$', views.search),        # 接收问题
    url(r'^search_port$', views.search_port),        # 接收问题

    url(r'^question$', views.question, name="question"),

    #视频课
    url(r'^$',views.search_answer,name="search_answer"),

    #自己测试
    # url(r'^test(\d+)$', views.test, name="test"), #位置参数
    url(r'^test', views.test), #位置参数
    # url(r'^test(?p<num>\d+)$', views.test, name="test"),   #关键字参数

    url(r'^login$', views.login, name="login"), #登录参数
    url(r'^login_check$', views.login_check, name="login_check"), #未知参数

    url(r'^ajax_test$', views.ajax_test, name="ajax_test"), #Ajax测试
    url(r'^ajax_handle$', views.ajax_handle), #Ajax数据接口

    url(r'^login_ajax$',views.login_ajax), #ajax登录
    url(r'^login_ajax_check$',views.login_ajax_check), #ajax登录验证

    url(r'^chuancan$',views.chuancan),  #给模板传参
    url(r'^show_ques',views.show_ques), #MVT案例
    url(r'^detail/(\d+)$',views.detail),  #显示答案信息
]
