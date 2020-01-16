from django.core.management.base import BaseCommand
from card.models.Card import Card
from card.models.CardType import CardType
from django.db.models import Q
import os
import base64
import json
from utils.ApiOcr import client
import requests
import shutil


class Command(BaseCommand):
    help = "upload image"

    def handle(self, *args, **options):
        Letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
        Number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                  'twelve', 'thirteen',
                  'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'number',
                  'triangle', 'square', 'rectangle', 'circle', 'black', 'white', 'color', 'red', 'purple', 'pink',
                  'yellow', 'orange', 'grey', 'green', 'brown', 'blue']
        Fruit = ['fruit', 'grape', 'cherry', 'strawberry', 'lemon', 'mango', 'peach', 'watermelon', 'pear', 'orange',
                 'apple', 'coconut', 'pineapple', 'banana', 'vegetable', 'beans', 'cabbage', 'cucumber', 'peas',
                 'pepper', 'mushroom',
                 'onion', 'eggplant', 'carrot', 'pumpkin', 'corn', 'potato', 'tomato']
        Food = ['cheese', 'sandwich', 'yoghourt', 'can', 'cup', 'water', 'honey', 'jam', 'kitchen', 'breakfast', 'wine',
                'fridge', 'milk',
                'egg', 'sausage', 'bread', 'chips', 'juice', 'cookies', 'ice cream', 'candy', 'egg tart', 'chocolate',
                'French fries', 'lunch', 'chicken', 'hot dog', 'hamburger', 'cola', 'dessert', 'cake', 'dinner', 'bowl',
                'spoon', 'bottle', 'knife', 'fork', 'plate', 'fish', 'soup', 'salad', 'beef', 'meat', 'rice', 'beer',
                'noodles', 'food']
        Animal = ['zoo', 'animal', 'giraffe', 'crocodile', 'squirrel', 'elephant', 'deer', 'bear', 'lion', 'otter',
                  'hippo', 'monkey',
                  'camel', 'zebra', 'tortoise', 'wolf', 'panda', 'fox', 'tiger', 'cock', 'chick', 'hen', 'dog', 'bird',
                  'mouse', 'ant',
                  'spider', 'snail', 'sheep', 'snake', 'rabbit', 'frog', 'horse', 'cow', 'duck', 'pig', 'cat', 'goat']
        Body = ['foot', 'knee', 'leg', 'body', 'tooth', 'mouth', 'nose', 'arm', 'hand', 'ear', 'eye', 'face', 'hair',
                'head', 'clothes',
                'cap', 'hat', 'shoes', 'ring', 'watch', 'necklace', 'glasses', 'bag', 'coat', 'pants', 'skirt', 'socks',
                'gloves',
                'T-shirt', 'shirt', 'dress', 'scarf', 'sweater']
        Family = ['love', 'uncle', 'son', 'sister', 'pet', 'mother', 'family', 'grandmother', 'grandfather', 'father',
                  'daughter', 'cousin',
                  'brother', 'aunt', 'friend', 'card', 'woman', 'women', 'toy', 'robot', 'princess', 'prince', 'person',
                  'people', 'men', 'man',
                  'balloon', 'clown', 'birthday party', 'child', 'boy', 'girl', 'baby']
        Home = ['home', 'room', 'doll', 'bed', 'pillow', 'bathroom', 'bedroom', 'mirror', 'clock', 'mat', 'quilt',
                'towel', 'closet', 'soap',
                'box', 'door', 'bath', 'photo', 'sofa', 'table', 'wall', 'lamp', 'flower', 'umbrella', 'desk', 'house',
                'window', 'study', 'living-room',
                'picture', 'key', 'cellphone', 'chair', 'television', 'computer', 'apartment']
        School = ['name', 'test', 'schoolbag', 'ruler', 'pencil', 'pen', 'paper', 'book', 'floor', 'eraser', 'class',
                  'student', 'teacher',
                  'classroom', 'crayon', 'blackboard', 'run', 'jump', 'football', 'ball', 'basketball', 'badminton',
                  'walk', 'play', 'table-tennis',
                  'sport', 'line', 'school', 'swim', 'sing', 'draw', 'shell', 'guitar', 'piano', 'kite', 'boat', 'sand',
                  'game', 'sea', 'beach', 'dance',
                  'music', 'art']
        Street = ['traffic light', 'bank', 'hotel', 'tree', 'bookshop', 'park', 'supermarket', 'sky', 'shop',
                  'restaurant', 'pram',
                  'policeman', 'doctor', 'driver', 'plane', 'taxi', 'motorbike', 'jeep', 'truck', 'car', 'bus', 'bike']
        Time = ['season', 'winter', 'autumn', 'summer', 'spring', 'snowman', 'rainbow', 'temperature', 'cold', 'cool',
                'hot', 'warm',
                'morning', 'afternoon', 'evening', 'sunny', 'day', 'moon', 'star', 'rainy', 'windy', 'cloudy', 'sun',
                'month', 'January',
                'February', 'March', 'April', 'May', 'June', 'July', 'Auguest', 'September', 'October', 'November',
                'December', 'week',
                'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        Sight = ['in', 'out', 'under', 'on', 'in front of', 'behind', 'between', 'down', 'up', 'touch', 'thank', 'tall',
                 'sorry',
                 'please', 'help', 'fine', 'hello', 'idea', 'favourite', 'new', 'goodbye', 'again', 'sit', 'stand',
                 'like', 'say', 'write',
                 'look', 'read', 'fly', 'eat', 'listen', 'drink', 'happy', 'sad', 'cry', 'laugh', 'shy', 'angry',
                 'scared', 'surprised',
                 'sleepy', 'thirsty', 'hungry', 'go', 'come', 'bad', 'good', 'stop', 'start', 'thin', 'fat', 'slow',
                 'fast', 'dry', 'wet',
                 'dirty', 'clean', 'weak', 'strong', 'short', 'long', 'hard', 'soft', 'small', 'big', 'close', 'open',
                 'few', 'many', 'old',
                 'young', 'wrong', 'right', 'begin', 'end']
        card_type = CardType.objects.get(id=84)
        i = 0
        for item in Fruit:
            i = i + 1
            Card.objects.create(name=item, picture='{}_20190814.png'.format(item), card_type=card_type,
                                am_word_voice='/audio/card/{}_20190814.mp3'.format(item), page_num=i)
