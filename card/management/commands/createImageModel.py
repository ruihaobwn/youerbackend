from card.models.Card import Card
from django.core.management.base import BaseCommand
import turicreate
import os


class Command(BaseCommand):
    help = "create image recognize model"

    def handle(self, *args, **options):
        all_cards = Card.objects.filter(card_type=1)
        image_array = turicreate.SArray(dtype=turicreate.Image)
        imageid_array = turicreate.SArray(dtype=int)
        index = 0
        for card in all_cards:
            if os.path.isfile(card.picture.path):
                image_path = card.picture.path
                print(image_path)
                card.recognize_id = index
                card.save()
                index += 1
                img = turicreate.Image(image_path)
                image_array = image_array.append(turicreate.SArray([img]))
                imageid_array = imageid_array.append(turicreate.SArray([card.id]))
        sf = turicreate.SFrame({'id': imageid_array, 'image': image_array})
        image_model = turicreate.image_similarity.create(sf)
        if image_model:
            image_model.save('image_model')
