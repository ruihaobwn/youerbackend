from django.contrib import admin
from card import models


@admin.register(models.ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'sup_type', 'sub_type', 'image')


@admin.register(models.CardType)
class CardTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'title', 'image_file', 'voice_num')


@admin.register(models.Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'page_num', 'picture', 'card_type', 'video')
    search_fields = ('name',)
    list_filter = ('card_type',)


