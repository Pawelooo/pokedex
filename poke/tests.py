from django.test import TestCase
from rest_framework.test import APIRequestFactory



class PokemonTestCase(TestCase):

    def test_create_pokemon(self):
        factory = APIRequestFactory()
        g
        request = factory.post('/api/pokemons/', {'name': 'charizard', 'attack': 29, 'block':5, 'kind': 'Ghost'})

