from django.db import models

# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length=60)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    def __str__(self):
        return f"""Loja: {self.nome}"""
    

class Produto(models.Model):
    nome = models.CharField(max_length=60)
    preco = models.FloatField()
    loja = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    home = models.BooleanField(default=1)
    def __str__(self):
        return f"{self.nome} da {self.loja}"

class Imagem(models.Model):
    img = models.CharField(max_length=200, default='')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    def __str__(self):
        return f"Imagem do produto {self.produto}"
 