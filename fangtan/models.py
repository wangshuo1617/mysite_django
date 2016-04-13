#-*-coding:utf-8-*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class duixiang(models.Model):
    picture=models.ImageField(blank=True)
    name=models.CharField(max_length=20)
    sex=models.CharField(max_length=10,choices=[('m',u'男'),('f',u'女')])
    university=models.CharField(max_length=20)
    grade=models.PositiveSmallIntegerField(choices=[(1,u'大一'),(2,'大二'),(3,'大三'),(4,'大四')])
    homeland=models.CharField(max_length=10)
    major=models.CharField(max_length=10)
    label=models.CharField(max_length=20)
    income=models.CharField(max_length=10,choices=[('poor',u'贫穷'),('normal',u'一般'),('rich',u'富裕'),('super',u'土豪')])
    elseinfo=models.TextField(blank=True)

    def __unicode__(self):
        return self.name+''+self.university

class report(models.Model):
    time=models.DateField()
    origin=models.FileField()
    ctic=models.TextField(blank=True)
    report_to=models.ForeignKey(duixiang,on_delete=models.CASCADE)

    def __unicode__(self):
        return unicode(self.time)+self.report_to.name
