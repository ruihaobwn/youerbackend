from django.db import models
from common.models import BaseModel
from .Book import Book, Volume
import os
from django.dispatch import receiver


class BookPage(BaseModel):
    title = models.CharField(verbose_name=u'主题', max_length=80, unique=True)
    picture = models.FileField(verbose_name=u'图片', max_length=80)
    audio_url = models.FileField(verbose_name=u'音频', max_length=80, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = '绘本页'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


@receiver(models.signals.post_delete, sender=BookPage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.picture:
        if os.path.isfile(instance.picture.path):
            os.remove(instance.picture.path)

    if instance.audio_url:
        if os.path.isfile(instance.audio_url.path):
            os.remove(instance.audio_url.path)


@receiver(models.signals.pre_save, sender=BookPage)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        card = BookPage.objects.get(pk=instance.pk)
        old_picture = card.picture
        old_audio_url = card.audio_url
    except BookPage.DoesNotExist:
        return False

    new_picture = instance.picture
    new_audio_url = instance.audio_url
    if old_picture and not old_picture == new_picture:
        if os.path.isfile(old_picture.path):
            os.remove(old_picture.path)

    if old_audio_url and not old_audio_url == new_audio_url:
        if os.path.isfile(old_audio_url.path):
            os.remove(old_audio_url.path)
