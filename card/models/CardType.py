from django.db import models
from common.models.BaseModel import BaseModel
from card.models.ProductType import ProductType


class CardType(BaseModel):
    title = models.CharField(verbose_name=u'卡片类别名称', max_length=80)
    image_file = models.FileField(verbose_name=u'图片')
    product = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    voice_num = models.IntegerField(verbose_name='发音数量', default=1)

    class Meta:
        verbose_name = '卡片类别'
        verbose_name_plural = '卡片类别'

    def __str__(self):
        return self.title
