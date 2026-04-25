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
    
class CarrinhoItem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey('Product', on_delete=models.CASCADE) # 'Produto' é o nome do seu outro model
    quantidade = models.PositiveIntegerField(default=1)
    data_adicionado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"