from django.db import models
from common.models.BaseModel import BaseModel
import os
from django.dispatch import receiver


class ProductType(BaseModel):
    SUP_TYPE_CHOICES = (
        ('English', '英文教具'),
        ('Chinese', '中文教具'),
    )
    sup_type = models.CharField(verbose_name=u'语言类型', max_length=80, choices=SUP_TYPE_CHOICES)
    sub_type = models.CharField(verbose_name=u'产品类别', max_length=80)
    image = models.FileField(verbose_name=u'图片')

    class Meta:
        verbose_name = '卡片产品类型'
        verbose_name_plural = '卡片产品类型'

    def __str__(self):
        return '{}-{}'.format(self.sup_type, self.sub_type)


@receiver(models.signals.post_delete, sender=ProductType)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=ProductType)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = ProductType.objects.get(pk=instance.pk).image
    except ProductType.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
