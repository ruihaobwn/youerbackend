from django.db import models
from common.models.BaseModel import BaseModel
import os
from django.dispatch import receiver


class Poster(BaseModel):
    TYPE_CHOICES = (
        ('Card', '单词页面'),
        ('Library', '绘本馆页面'),
        ('Video', '视频页面'),
    )
    name = models.CharField(verbose_name=u'名称', max_length=100)
    type = models.CharField(verbose_name=u'类型', choices=TYPE_CHOICES, max_length=100)
    image = models.FileField(verbose_name=u'图片', upload_to='poster')
    link_url = models.CharField(verbose_name=u'跳转地址', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = '海报图'
        verbose_name_plural = '海报图'


@receiver(models.signals.post_delete, sender=Poster)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=Poster)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = Poster.objects.get(pk=instance.pk).image
    except Poster.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
