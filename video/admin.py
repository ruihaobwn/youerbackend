from django.contrib import admin
from video import models


@admin.register(models.VideoType)
class VideoTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_file')


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_file', 'video_type', 'has_subvideo')


@admin.register(models.SubVideo)
class SubVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'video_url', 'video')
