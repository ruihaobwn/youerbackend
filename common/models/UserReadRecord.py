from django.db import models
from common.models import BaseModel


# 记录用户读到书本的位置
# class UserReadRecord(BaseModel):
#     name = models.CharField(verbose_name=u'绘本名称', max_length=80, unique=True)
#     picture = models.FileField(verbose_name=u'绘本图片', max_length=80)
#     book_type = models.ForeignKey(BookType, on_delete=models.CASCADE)
#     has_subbook = models.BooleanField(verbose_name='是否有子绘本', default=False)
#
#     class Meta:
#         verbose_name = '绘本'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name
