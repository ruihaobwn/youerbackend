from django.core.management.base import BaseCommand
from card.models.Card import Card
from django.db.models import Q
import os
import base64
import json
from utils.ApiOcr import client
import requests


class Command(BaseCommand):
    help = "sync word to database"

    def handle(self, *args, **options):
        no_recognize_cards = Card.objects.filter(Q(recognize_word__isnull=True)|Q(recognize_word=''))
        for card in no_recognize_cards:
            if os.path.isfile(card.picture.path):
                image_path = card.picture.path
                print(card.name)
                with open(image_path, mode='rb') as f:
                    image_body = f.read()
                if image_body:
                    try:
                        res = client.basicGeneral(image_body)
                        text = res["words_result"][0]["words"]
                        card.recognize_word = text
                        words_dict_list = res["words_result"]
                        words_list = []
                        for item in words_dict_list:
                            words_list.append(item["words"])
                        print(words_list)
                        card.recognize_text = json.dumps(words_list)
                        card.save()
                    except requests.HTTPError as e:
                        print(e)


            # image_base64Str = base64.b64encode(image_body).decode()
            # tencent_api = OCR.TencentAPIMsg()
            # req_dict = {"image": image_base64Str}
            # sign = tencent_api.gen_req_dict(req_dict=req_dict)
            # req_dict["sign"] = sign
            # url = "https://api.ai.qq.com/fcgi-bin/ocr/ocr_generalocr"
            # print(card.name)
            # try:
            #     resp = requests.post(url, data=req_dict)
            #     resp.raise_for_status()
            #     results = resp.json()
            #     if results.get('ret') == 0:
            #         data = results["data"]
            #         recognize_str = ''
            #         for item in data["item_list"]:
            #             recognize_str += item['itemstring']
            #         print(recognize_str)
            #         card.recognize_word = recognize_str
            #         card.save()
            # except requests.HTTPError as e:
            #     print(e)