from django.contrib import admin
from video import models


@admin.register(models.VideoType)
class VideoTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_file', 'id')


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_file', 'video_type', 'has_subvideo', 'id')


@admin.register(models.SubVideo)
class SubVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url', 'video', 'id')
