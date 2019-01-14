from django.db import models
from common.models import BaseModel
from .CardType import CardType
import os
from django.dispatch import receiver


class Card(BaseModel):
    name = models.CharField(verbose_name=u'图片名称', max_length=80, unique=True)
    picture = models.FileField(verbose_name=u'卡片图片', max_length=80)
    card_type = models.ForeignKey(CardType, on_delete=models.CASCADE)
    video = models.FileField(verbose_name=u'卡片视频', upload_to='video/card', max_length=80, null=True, blank=True)

    class Meta:
        verbose_name = '卡片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


@receiver(models.signals.post_delete, sender=Card)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.picture:
        if os.path.isfile(instance.picture.path):
            os.remove(instance.picture.path)
    if instance.video:
        if os.path.isfile(instance.video.path):
            os.remove(instance.video.path)


@receiver(models.signals.pre_save, sender=Card)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        card = Card.objects.get(pk=instance.pk)
        old_picture = card.picture
        old_video = card.video

    except Card.DoesNotExist:
        return False

    new_picture = instance.picture
    new_video = instance.video
    if old_picture and not old_picture == new_picture:
        if os.path.isfile(old_picture.path):
            os.remove(old_picture.path)
    if old_video and not old_video == new_video:
        if os.path.isfile(old_video.path):
            os.remove(old_video.path)
