# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.

@cache_page(60 * 15)
def my_view(request):
    queryset=[1,2,3,4,5]
    return render(request, 'index.html', {'queryset':queryset})

'''
cache_page 接受了一个参数：timeout，单位为秒。
在上例中 my_view() 视图的结构将被缓存 15 分钟（注意为了提高可读性，我们写了 60 * 15）。
'''