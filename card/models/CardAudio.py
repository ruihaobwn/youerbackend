from django.db import models
from common.models.BaseModel import BaseModel
from ..models import Card
import os
from django.dispatch import receiver


class CardAudio(BaseModel):
    """CardResource include picture, voice
    """
    RESOURCE_TYPT_CHOICES = (
        ('Word', '单词'),
        ('Sentence', '句子'),
    )
    type = models.CharField(verbose_name=u'音频类型', choices=RESOURCE_TYPT_CHOICES, max_length=25)
    url = models.FileField(verbose_name=u'资源地址', upload_to='audio/card', max_length=80)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '卡片音频'
        verbose_name_plural = '卡片音频'


@receiver(models.signals.post_delete, sender=CardAudio)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.url:
        if os.path.isfile(instance.url.path):
            os.remove(instance.url.path)


@receiver(models.signals.pre_save, sender=CardAudio)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = CardAudio.objects.get(pk=instance.pk).url
    except CardAudio.DoesNotExist:
        return False

    new_file = instance.url
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
