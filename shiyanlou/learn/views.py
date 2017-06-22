# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm

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
    c = a+b
    return HttpResponse(str(a+b))
