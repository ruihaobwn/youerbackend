from django.db import models
from common.models.BaseModel import BaseModel
import os
from django.dispatch import receiver
from .Video import Video


class SubVideo(BaseModel):
    title = models.CharField(verbose_name=u'名称', max_length=80)
    video_url = models.FileField(verbose_name=u'视频源', max_length=80)
    image_url = models.FileField(verbose_name=u'展示图片', max_length=80)
    video = models.ForeignKey(Video, verbose_name='所属视频', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(verbose_name='描述')

    class Meta:
        verbose_name = '子视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


@receiver(models.signals.post_delete, sender=SubVideo)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.video_url:
        if os.path.isfile(instance.video_url.path):
            os.remove(instance.video_url.path)
    if instance.image_url:
        if os.path.isfile(instance.image_url.path):
            os.remove(instance.image_url.path)


@receiver(models.signals.pre_save, sender=SubVideo)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = Video.objects.get(pk=instance.pk).video_url
        old_image = Video.objects.get(pk=instance.pk).image_url
    except Video.DoesNotExist:
        return False

    new_file = instance.video_url
    new_image = instance.image_url
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
