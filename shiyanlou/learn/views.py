# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    string =u"SJ"
    list1 = ['1','2','3','4']
    return render(request, 'learn/home.html',{'string':string,'list1':list1})