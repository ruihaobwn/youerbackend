from django.core.management.base import BaseCommand
from card.models.Card import Card
from django.db.models import Q
import os
import base64
from utils.CRS import CRS


class Command(BaseCommand):
    help = "sync image to cloud recognition service"

    def handle(self, *args, **options):
        no_target_cards = Card.objects.filter(Q(image_traget_id__isnull=True) | Q(image_traget_id=''))
        for card in no_target_cards:
            if os.path.isfile(card.picture.path):
                image_path = card.picture.path
                with open(image_path, mode='rb') as f:
                    image_body = f.read()
                if image_body:
                    params = {
                        "image": base64.b64encode(image_body).decode(),
                        "name": 'maize',
                        "size": "8",
                        "meta": 10,
                        "type": "ImageTarget",
                    }
                    res = CRS().create_target(params)
                    if res.statusCode == 0:
                        result = res['result']
                        target_id = result['targetId']
                        card.image_traget_id = target_id
                        card.save()

