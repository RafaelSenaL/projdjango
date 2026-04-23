#models

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default= 1)
    marca = models.CharField(max_length=50, default='Genérica')
    preço = models.FloatField(default=0)

    def __str__(self):
        return self.nome