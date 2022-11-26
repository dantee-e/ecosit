from django.shortcuts import render
from ecosite.models import Produto, Imagem

# Create your views here.


def index(request):
    produtos=[]
    for i in Produto.objects.filter(home=1):
        imag = Imagem.objects.get(produto=i)
        produtos.append([i.nome, i.preco, imag.img])
        print(imag.img)
    return render(request, "ecosite/index.html", {
        "produtos": produtos

    }) 