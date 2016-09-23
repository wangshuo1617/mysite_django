#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class wxwz(models.Model):
    post_date = models.DateField()
    pos = models.PositiveSmallIntegerField()
    title = models.CharField(max_length = 100)
    title_type = models.CharField(max_length=10,choices=[('zy','直言'),('as','暗示'),('xz','新知'),('tw','提问'),('ml','命令'),('pd','盘点'),('rx','人性'),('dr','代入'),('jq','节气'),('rd','热点'),('zht','知乎体'),('dbkz','对比夸张')])
    con_type = models.CharField(max_length=10)
    share = models.IntegerField(blank = True)
    view = models.IntegerField(blank = True)
    like = models.IntegerField(blank = True)
    forward = models.IntegerField(blank = True)
    score = models.IntegerField(blank = True)
    url = models.CharField(blank = True, max_length = 200)
    author = models.CharField(blank = True, max_length = 10)
    center = models.CharField(blank = True, max_length = 10)

    def __unicode__(self):
        return self.title
