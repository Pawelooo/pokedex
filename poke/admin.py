from django.contrib import admin

# Register your models here.
from poke.models import KindOfPokemon, Pokemon

admin.site.register(KindOfPokemon)
admin.site.register(Pokemon)