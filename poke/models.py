from django.db import models


class KindOfPokemon(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    kind = models.ForeignKey(KindOfPokemon, on_delete=models.PROTECT)
    attack = models.IntegerField()
    block = models.IntegerField()

    def __str__(self):
        return self.name, self.kind
