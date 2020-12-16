from django.contrib.gis.db import models

class Escola(models.Model):
    nome = models.CharField(max_length=200)
    geom = models.PointField()

    def __str__(self):
        return self.nome
