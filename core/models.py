from django.contrib.gis.db import models

class Escola(models.Model):
    """
    Modelo que representa uma escola
    """

    nome = models.CharField(max_length=200)
    geom = models.PointField()

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
    

