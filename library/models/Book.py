from django.db import models
from common.models import BaseModel
from .BookType import BookType
import os
from django.dispatch import receiver


# 卷 一卷中有多本书
class Volume(BaseModel):
    name = models.CharField(verbose_name=u'绘本名称', max_length=80, unique=True)
    picture = models.FileField(verbose_name=u'绘本图片', max_length=80)
    book_type = models.ForeignKey(BookType, verbose_name='绘本类别', on_delete=models.CASCADE)
    has_subbook = models.BooleanField(verbose_name='是否有子绘本', default=False)

    class Meta:
        verbose_name = '绘本'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 绘本
class Book(BaseModel):
    name = models.CharField(verbose_name=u'主题', max_length=80, unique=True)
    picture = models.FileField(verbose_name=u'子绘本图片', max_length=80)
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE)
    description = models.TextField(verbose_name=u'子绘本描述')

    class Meta:
        verbose_name = '子绘本'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


@receiver(models.signals.post_delete, sender=Volume)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.picture:
        if os.path.isfile(instance.picture.path):
            os.remove(instance.picture.path)


@receiver(models.signals.pre_save, sender=Volume)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        card = Volume.objects.get(pk=instance.pk)
        old_picture = card.picture

    except Volume.DoesNotExist:
        return False

    new_picture = instance.picture
    if old_picture and not old_picture == new_picture:
        if os.path.isfile(old_picture.path):
            os.remove(old_picture.path)


@receiver(models.signals.post_delete, sender=Book)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.picture:
        if os.path.isfile(instance.picture.path):
            os.remove(instance.picture.path)


@receiver(models.signals.pre_save, sender=Book)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        card = Book.objects.get(pk=instance.pk)
        old_picture = card.picture

    except Book.DoesNotExist:
        return False

    new_picture = instance.picture
    if old_picture and not old_picture == new_picture:
        if os.path.isfile(old_picture.path):
            os.remove(old_picture.path)
