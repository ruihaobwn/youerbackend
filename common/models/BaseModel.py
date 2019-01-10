from django.db import models
from common.models.BaseManager import BaseManager


class BaseModel(models.Model):
    comment = models.TextField(verbose_name='备注', blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False, db_index=True)

    objects = BaseManager()

    class Meta:
        abstract = True
