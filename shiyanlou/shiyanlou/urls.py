"""shiyanlou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Hello import views as Hello_views
from calc import views as calc_views
from learn import views as learn_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', Hello_views.index),
    url(r'^django/', Hello_views.index2),
    url(r'^add/$',calc_views.add, name='add'),
    url(r'^add2/(\d+)/(\d+)/$',calc_views.add2,name='add2'),
    url(r'^learn/home/', learn_views.home,name='home'),

]