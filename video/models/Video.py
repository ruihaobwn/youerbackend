from django.db import models
from common.models.BaseModel import BaseModel
from .VideoType import VideoType
import os
from django.dispatch import receiver


class Video(BaseModel):
    title = models.CharField(verbose_name=u'名称', max_length=80)
    image_file = models.FileField(verbose_name=u'图片', max_length=80)
    video_url = models.FileField(verbose_name=u'视频源',upload_to='video/movie', max_length=80, null=True, blank=True)
    video_type = models.ForeignKey(VideoType, verbose_name='视频类型', on_delete=models.CASCADE)
    has_subvideo = models.BooleanField(verbose_name=u'是否有子视频', default=False)

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


@receiver(models.signals.post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image_file:
        if os.path.isfile(instance.image_file.path):
            os.remove(instance.image_file.path)
    if instance.video_url:
        if os.path.isfile(instance.video_url.path):
            os.remove(instance.video_url.path)


@receiver(models.signals.pre_save, sender=Video)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = Video.objects.get(pk=instance.pk).image_file
        old_video = Video.objects.get(pk=instance.pk).video_url
    except Video.DoesNotExist:
        return False

    new_file = instance.image_file
    new_video = instance.video_url
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
    if not old_video == new_video:
        if os.path.isfile(old_video.path):
            os.remove(old_video.path)
