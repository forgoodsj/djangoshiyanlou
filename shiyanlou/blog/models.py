# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField('title', max_length=256)
    category = models.CharField('category', max_length=50, blank = True)
    content = models.TextField('content',blank = True, null = True)

    pub_date = models.DateTimeField('publish-time', auto_now_add=True, editable = True)
    update_time = models.DateTimeField('update-time',auto_now_add=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-update_time']

#ceshi