#-*- coding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField

class TypeInfo(models.Model):
    ttitle =models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle.encode('utf-8')

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=40)#标题
    gpic=models.ImageField(upload_to='df_goods')#图片
    gprice = models.DecimalField(max_digits=6,decimal_places=2)#价格
    isDelete = models.BooleanField(default=False)#是否删除
    gunit=models.CharField(max_length=20)#单位
    gclick=models.IntegerField()#点击量
    gabstract =models.CharField(max_length=200)#简介
    gstock=models.IntegerField()#库存
    gcontent=HTMLField()#详情页
    #gadv=models.IntegerField()#是否被推荐
    gtype=models.ForeignKey(TypeInfo)

    def __str__(self):
        return self.gtitle.encode('utf-8')










