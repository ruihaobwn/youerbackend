from django.db import models
from common.models.BaseModel import BaseModel
import os
from django.dispatch import receiver


class BookType(BaseModel):
    title = models.CharField(verbose_name=u'类别名称', max_length=80)
    image_file = models.FileField(verbose_name=u'图片')

    class Meta:
        verbose_name = '绘本类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        
        return self.title


@receiver(models.signals.post_delete, sender=BookType)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image_file:
        if os.path.isfile(instance.image_file.path):
            os.remove(instance.image_file.path)


@receiver(models.signals.pre_save, sender=BookType)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = BookType.objects.get(pk=instance.pk).image_file
    except BookType.DoesNotExist:
        return False

    new_file = instance.image_file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
