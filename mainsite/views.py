# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Post

# 将ascill码 转为 utf-8
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
      reload(sys)
      sys.setdefaultencoding(default_encoding)



# Create your views here.
def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    # render将数据传输到模板指定位置显示
    html = template.render(locals())
    return HttpResponse(html)

# def homepage(request):
#     posts = Post.objects.all()
#     post_lists = list()
#     for count, post in enumerate(posts):
#         post_lists.append("No.{}:".format(str(count)) + str(post) + "<br>")
#         print(post_lists)
#         post_lists.append("<samll>"+str(post.body)+"</small><br><br>")   # 标签呈现小号字体效果、换行效果
#     return HttpResponse(post_lists)