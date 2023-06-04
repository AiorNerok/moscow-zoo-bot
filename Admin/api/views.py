from ninja import NinjaAPI
from .models import Animals
from random import choice
from ninja import Schema

api = NinjaAPI()

class RandomAnimalsSchema(Schema):
    name: str
    src: str
    link_to_more_info: str

@api.get('/', response=RandomAnimalsSchema)
def randomAnimals(_):
    res = choice(Animals.objects.all())
    
    return res