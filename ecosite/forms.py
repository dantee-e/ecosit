from django import forms


class NovoProduto(forms.Model):
    nome = forms.CharField(max_length=60)
    preco = forms.FloatField()
    home = forms.BooleanField(default=1)