# -*- coding: utf-8 -*-
__author__ = 'chanran'

import urllib
import urllib2
import random

time = input("请输入要刷多少票：")
i = 1
while (i<=time):
    i = i+1
    #数据
    name = random.randrange(100000,99999999,1)
    password = random.randrange(100000,99999999,1)
    try:
        #注册
        url = 'http://jobs.jt-wireless.com/toClientUserRegisterSubmit.action'
        data = {'hrClientUser.username':name,'hrClientUser.password':password,'sex':1}
        url_values = urllib.urlencode(data)
        request = urllib2.Request(url,url_values)
        response = urllib2.urlopen(request)
        #登录
        url = 'http://jobs.jt-wireless.com/ClientUserLogin.action'
        data = {'username':name,'password':password}
        url_values = urllib.urlencode(data)
        request = urllib2.Request(url,url_values)
        response = urllib2.urlopen(request)
        data = response.geturl()
        datas = data.split(";")
        Cookie = datas[1]

        Cookie = Cookie.replace("jsessionid", "JSESSIONID")

        #投票
        url = 'http://jobs.jt-wireless.com/addSignUpActivityInfo.action'
        data = {'type':3,'id':42} #参数
        url_values = urllib.urlencode(data)
        request = urllib2.Request(url,url_values)
        request.add_header('Cookie',Cookie) #添加登录的cookie到头文件
        response = urllib2.urlopen(request)
        page = response.read()

        #将投票过的账号和密码写入文件
        file = open('user.txt',"a+")
        user = " username="+str(name)+" password="+str(password)+"\n"
        file.write(user)
        file.close()
    except IndexError:
        file = open("alreadyRegister.txt","a+")
        user = " username="+str(name)+" password="+str(password)+"\n"
        file.write(user)
        file.close()
        pass
