from django.contrib import admin
from library import models


@admin.register(models.BookType)
class BookTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')


@admin.register(models.Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'picture', 'book_type', 'id')
    list_filter = ('book_type',)


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'picture', 'volume', 'description', 'id')


@admin.register(models.BookPage)
class BookPageeAdmin(admin.ModelAdmin):
    list_display = ('id', 'picture', 'audio_url', 'book', 'volume', 'page_num')
    list_filter = ('volume', 'book')
