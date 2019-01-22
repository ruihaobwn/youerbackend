from django.contrib import admin
from library import models


@admin.register(models.BookType)
class BookTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_file')


@admin.register(models.Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'picture', 'book_type')


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'picture', 'volume', 'description')


@admin.register(models.BookPage)
class BookPageeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'picture', 'audio_url', 'book', 'volume')
