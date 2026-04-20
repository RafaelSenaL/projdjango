from django.db import models

class Product(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=50, default='Genérica')
    preço = models.FloatField(default=0)

    def __str__(self):
        return self.nome