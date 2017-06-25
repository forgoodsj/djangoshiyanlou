# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from subprocess import check_output

# Create your views here.
def home(request):
    string =u"SJ"
    list1 = ['1','2','3','4']
    return render(request, 'learn/home.html',{'string':string,'list1':list1})

def index(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():#如果数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a)+int(b)))
        else:
            return HttpResponse("error")
    else:
        form = AddForm()
    return render(request, 'learn/index.html',{'form':form})

def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

def email(request):
    receiver = '418025351@qq.com'    # 第三方 SMTP 服务
    mail_host="smtp.126.com"  #设置服务器
    mail_user="forgoodsj@126.com"#用户名
    mail_pass="1234qwer"   #口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格
    sender = mail_user
    receivers = [receiver]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText('这里是叔叔的爱心,叔叔正在尝试用爱发电，如果方法送成功，就代表叔叔的爱能发电啦！' ,'plain', 'utf-8')
    message['From'] = Header(mail_user, 'utf-8')
    message['To'] =  Header(str(receivers), 'utf-8')

    subject = u'baby我最爱你了！'
    message['Subject'] = Header(subject, 'utf-8')

    try:
       smtpObj = smtplib.SMTP_SSL(mail_host, 465)
       smtpObj.login(mail_user,mail_pass)
       smtpObj.sendmail(sender, receivers, message.as_string())
       smtpObj.quit()
       print ("邮件发送成功")
       return HttpResponse(u"邮件发送成功")
    except smtplib.SMTPException,e:
       print (e)
       return HttpResponse(e)