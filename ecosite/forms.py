from django.forms import ModelForm
from django import forms
from ecosite.models import Produto, Imagem, Empresa, Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'home']
    
class ImagemForm(ModelForm):
    class Meta: 
        model = Imagem
        fields = '__all__'


class NovoUsuarioForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ['email', 'first_name', 'last_name', 'celular', 'password1', 'password2']

"""
class NovaEmpresaform(ModelForm):
    class Meta:
        model = Empresa
        fields = ('CNPJ', 'nome', 'telefone', 'email')
"""