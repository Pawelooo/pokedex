from django.test import TestCase
from rest_framework.test import APIRequestFactory

from poke.models import KindOfPokemon


class PokemonTestCase(TestCase):

    def test_create_pokemon(self):
        factory = APIRequestFactory()
        ghost = KindOfPokemon.objects.create(name='Ghost')
        request = factory.post('/api/pokemons/', {'name': 'charizard', 'attack': 29, 'block':5, 'kind': ghost})

