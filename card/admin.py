from django.contrib import admin
from card import models


@admin.register(models.ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'sup_type', 'sub_type', 'image')


@admin.register(models.CardType)
class CardTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_file', 'voice_num')


@admin.register(models.Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'picture', 'card_type', 'video')


@admin.register(models.CardAudio)
class CardResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'url')

