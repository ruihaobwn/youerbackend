from django.core.management.base import BaseCommand
from card.models.Card import Card
from django.db.models import Q
import os
import base64
import json
from utils.ApiOcr import client
import requests
import shutil


class Command(BaseCommand):
    help = "fetch card from database"

    def handle(self, *args, **options):
        export_dir = '/root/bak'
        no_recognize_cards = Card.objects.filter(card_type__product__sup_type='English', am_word_voice__isnull=False)
        i = 0
        for card in no_recognize_cards:
            if os.path.isfile(card.picture.path) and os.path.isfile(card.am_word_voice) and os.path.isfile(
                    card.am_sentence_voice):
                i = i + 1
                image_path = card.picture.path
                print(image_path)
                word_path = card.am_word_voice.path
                sentence_path = card.am_sentence_voice.path
                image_dst = '{}/{}.jpg'.format(export_dir, i)
                word_dst = '{}/{}.mp3'.format(export_dir, i)
                sentence_dst = '{}/{}_sen.mp3'.format(export_dir, i)
                # shutil.copy(image_path, image_dst)
                # shutil.copy(word_path, word_dst)
                # shutil.copy(sentence_path, sentence_dst)
