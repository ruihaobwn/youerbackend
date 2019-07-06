from django.db import models
from common.models.BaseModel import BaseModel
import os
from django.dispatch import receiver


class BookType(BaseModel):
    title = models.CharField(verbose_name=u'类别名称', max_length=80)

    class Meta:
        verbose_name = '绘本类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        
        return self.title

