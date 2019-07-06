from django.core.management.base import BaseCommand
from card.models.Card import Card
from django.db.models import Q
import os
import base64
from utils.CRS import CRS


class Command(BaseCommand):
    help = "sync image to cloud recognition service"

    def handle(self, *args, **options):
        no_target_cards = Card.objects.filter(image_traget_id__isnull=True)
        for card in no_target_cards:
            if os.path.isfile(card.picture.path):
                image_path = card.picture.path
                with open(image_path, mode='rb') as f:
                    image_body = f.read()
                if image_body:
                    params = {
                        "image": base64.b64encode(image_body).decode(),
                        "name": card.name,
                        "size": "8",
                        "meta": card.id,
                        "type": "ImageTarget",
                    }
                    try:
                        res = CRS().create_target(params)
                        if res['statusCode'] == 0:
                            result = res['result']
                            target_id = result['targetId']
                            card.image_traget_id = target_id
                            card.save()
                        else:
                            print("相似:"+card.name)
                    except Exception as e :
                        print("错误" + card.name)
