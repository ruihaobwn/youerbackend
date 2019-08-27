from django.db import models
from common.models import BaseModel
from .CardType import CardType
import os
from django.dispatch import receiver
from utils.CRS import CRS


class Card(BaseModel):
    name = models.CharField(verbose_name=u'图片名称', max_length=80)
    picture = models.FileField(verbose_name=u'卡片图片', max_length=80)
    card_type = models.ForeignKey(CardType, verbose_name='卡片类型', on_delete=models.CASCADE)
    en_word_voice = models.FileField(verbose_name=u'英式单词发音', upload_to='audio/card', max_length=80, null=True, blank=True)
    am_word_voice = models.FileField(verbose_name=u'美式单词发音', upload_to='audio/card', max_length=80, null=True, blank=True)
    en_sentence_voice = models.FileField(verbose_name=u'英式句子发音', upload_to='audio/card', null=True, blank=True,
                                      max_length=80)
    am_sentence_voice = models.FileField(verbose_name=u'美式句子发音', upload_to='audio/card', null=True, blank=True,
                                      max_length=80)
    video = models.FileField(verbose_name=u'卡片视频', upload_to='video/card', max_length=80, null=True, blank=True)
    page_num = models.IntegerField(verbose_name=u'页码', default=0)
    recognize_word = models.CharField(verbose_name=u'识别文字', max_length=100, null=True, blank=True)
    recognize_text = models.TextField(verbose_name=u'所有文字',null=True,blank=True)
    recognize_id = models.IntegerField(verbose_name=u'识别ID', null=True, blank=True)

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
            CRS().delete_target(instance.image_traget_id)
            instance.image_traget_id = None
    if instance.en_word_voice:
        if os.path.isfile(instance.en_word_voice.path):
            os.remove(instance.en_word_voice.path)
    if instance.am_word_voice:
        if os.path.isfile(instance.am_word_voice.path):
            os.remove(instance.am_word_voice.path)
    if instance.en_sentence_voice:
        if os.path.isfile(instance.en_sentence_voice.path):
            os.remove(instance.en_sentence_voice.path)
    if instance.am_sentence_voice:
        if os.path.isfile(instance.am_sentence_voice.path):
            os.remove(instance.am_sentence_voice.path)
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
        old_en_word_voice = card.en_word_voice
        old_am_word_voice = card.am_word_voice
        old_en_sentence_voice = card.en_sentence_voice
        old_am_sentence_voice = card.am_sentence_voice
        old_video = card.video
    except Card.DoesNotExist:
        return False

    new_picture = instance.picture
    new_en_word_voice = instance.en_word_voice
    new_am_word_voice = instance.am_word_voice
    new_en_sentence_voice = instance.en_sentence_voice
    new_am_sentence_voice = instance.am_sentence_voice
    new_video = instance.video
    if old_picture and not old_picture == new_picture:
        if os.path.isfile(old_picture.path):
            os.remove(old_picture.path)
            CRS().delete_target(instance.image_traget_id)
            instance.image_traget_id = None
    if old_en_word_voice and not old_en_word_voice == new_en_word_voice:
        if os.path.isfile(old_en_word_voice.path):
            os.remove(old_en_word_voice.path)
    if old_am_word_voice and not old_am_word_voice == new_am_word_voice:
        if os.path.isfile(old_am_word_voice.path):
            os.remove(old_am_word_voice.path)
    if old_en_sentence_voice and not old_en_sentence_voice == new_en_sentence_voice:
        if os.path.isfile(old_en_sentence_voice.path):
            os.remove(old_en_sentence_voice.path)
    if old_am_sentence_voice and not old_am_sentence_voice == new_am_sentence_voice:
        if os.path.isfile(old_am_sentence_voice.path):
            os.remove(old_am_sentence_voice.path)
    if old_video and not old_video == new_video:
        if os.path.isfile(old_video.path):
            os.remove(old_video.path)
