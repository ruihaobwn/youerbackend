from django.contrib import admin
from common import models


@admin.register(models.Poster)
class PosterAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'image', 'link_url')
