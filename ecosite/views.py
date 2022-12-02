from django.shortcuts import render, redirect
from ecosite.models import Produto, Imagem, Empresa
from ecosite.forms import ProdutoForm, ImagemForm, NovoUsuarioForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.


def index(request):
    produtos=[]
    for i in Produto.objects.filter(home=1):
        try:
            imag = Imagem.objects.filter(produto=i)[0].img
        except:
            imag = 0
        produtos.append([i.nome, i.preco, imag])
    if request.user.is_authenticated:
        if request.user.is_proprietario:
            return HttpResponse('proprietario')
        else:
            return HttpResponse('n proprietario')
        return render(request, "ecosite/index_autenticado.html", {
            "produtos": produtos,
            "message": 'Usuario autenticado',
        })
    else:
        return render(request, "ecosite/index.html", {
            "produtos": produtos,
            "message": 'Usuario nao autenticado',
        })


def criar_usuario(request):
    form = NovoUsuarioForm()
    if request.method == 'POST':
        form = NovoUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'ecosite/criar_usuario.html', {
        'form':form
    })


def addprod(request, nome_empresa):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    formprod = ProdutoForm()
    empresa = Empresa.objects.get(nome=nome_empresa)
    if request.method=='POST':
        formprod = ProdutoForm(request.POST)
        if formprod.is_valid():
            obj = formprod.save(commit=False)
            obj.loja = empresa
            obj.save()

    return render(request, 'ecosite/addprod.html', 
    {
        'empresa': empresa,
        'formprod': formprod
    })

def addimg(request, nome_empresa):
    if request.method=='POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')

    else:
        form = ImagemForm()
    return render(request, 'ecosite/addimg.html', 
    {
        'form': form
    })
            


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'ecosite/login.html', {
                'message': 'Credenciais invalidas'
            })
    return render(request, 'ecosite/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'ecosite/login.html')

def criar_empresa(request):
    form = NovoUsuarioForm()
    if request.method == 'POST':
        form = NovoUsuarioForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
        
    return render(request, 'ecosite/criar_empresa.html', {
        'form': form
    })