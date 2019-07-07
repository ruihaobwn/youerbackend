from django.contrib import admin
from card import models


@admin.register(models.ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('sup_type', 'sub_type', 'image', 'id')


@admin.register(models.CardType)
class CardTypeAdmin(admin.ModelAdmin):
    list_display = ('product','tag','tag_order', 'title', 'image_file', 'voice_num', 'id')
    search_fields = ('title',)
    list_filter = ('product',)


@admin.register(models.Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'page_num', 'picture', 'card_type', 'video', 'id')
    search_fields = ('name',)
    list_filter = ('card_type',)
