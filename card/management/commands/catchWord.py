from django.core.management.base import BaseCommand
from card.models.Card import Card
from django.db.models import Q
import os
import base64
import json
from utils.ApiOcr import client
import requests


class Command(BaseCommand):
    def handle(self, *args, **options):
        path = '/root/image'
        files = os.listdir(path)
        fo = open('word.txt', 'w+')
        for file in files:
            image_path = path + '/' + file
            with open(image_path, mode='rb') as f:
                image_body = f.read()
            if image_body:
                try:
                    res = client.basicGeneral(image_body)
                    words_dict_list = res["words_result"]
                    for item in words_dict_list:
                        print(item["words"])
                        fo.write(item["words"])
                except requests.HTTPError as e:
                    print(e)
        fo.close()
