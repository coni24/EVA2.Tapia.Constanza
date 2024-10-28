from django.db import models

class Entrada(models.Model):
    Categoria = models.CharField(max_length = 50)
    Descripcion = models.CharField(max_length = 50)
    NumeroAsiento = models.IntegerField()
    Precio = models.IntegerField()
    Sector = models.CharField(max_length = 50)
