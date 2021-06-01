from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    kind = models.CharField(max_length=20)
    attack = models.IntegerField()
    block = models.IntegerField()

    def __str__(self):
        return self.name, self.kind
