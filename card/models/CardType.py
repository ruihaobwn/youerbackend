from django.db import models
from common.models.BaseModel import BaseModel
from card.models.ProductType import ProductType
import os
from django.dispatch import receiver


class CardType(BaseModel):
    title = models.CharField(verbose_name=u'卡片类别名称', max_length=80)
    image_file = models.FileField(verbose_name=u'图片')
    product = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    voice_num = models.IntegerField(verbose_name='发音数量', default=1)

    class Meta:
        verbose_name = '卡片类别'
        verbose_name_plural = '卡片类别'

    def __str__(self):
        return '{}-{}'.format(self.product, self.title)


@receiver(models.signals.post_delete, sender=CardType)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image_file:
        if os.path.isfile(instance.image_file.path):
            os.remove(instance.image_file.path)


@receiver(models.signals.pre_save, sender=CardType)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = CardType.objects.get(pk=instance.pk).image_file
    except ProductType.DoesNotExist:
        return False

    new_file = instance.image_file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
