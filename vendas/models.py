#models

from django.db import models
from PIL import Image
from django.contrib.auth.models import User

class Product(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default= 1)
    marca = models.CharField(max_length=50, default='Genérica')
    preço = models.FloatField(default=0)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='produtos/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.imagem:
            img = Image.open(self.imagem.path)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            img.thumbnail((800, 800))
            img.save(self.imagem.path, "JPEG", quality=70, optimize=True)
    def __str__(self):
        return self.nome
    
class CarrinhoItem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    data_adicionado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"
    
class Contact(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.assunto}"