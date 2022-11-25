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
    def __str__(self):
        return f"{self.nome} por {self.preco}"
    
