from django.shortcuts import render, redirect
from ecosite.models import Produto, Imagem, Empresa
from ecosite.forms import ProdutoForm, ImagemForm, NovoUsuarioForm, NovaEmpresaForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.


def index_render(request, alert_logado):
    produtos=[]
    for i in Produto.objects.filter(home=1):
        try:
            imag = Imagem.objects.filter(produto=i)[0].img
        except:
            continue
        produtos.append([i.nome, i.preco, imag, i.descricao])
    if request.user.is_authenticated:
        return render(request, "ecosite/index_autenticado.html", {
            
            "produtos": produtos,
            "message": 'Usuario autenticado',
            "recem_logado": alert_logado,
            "is_proprietario": request.user.is_proprietario,
        })
        
    else:
        return render(request, "ecosite/index_novo.html", {
            "produtos": produtos,
        })

def index(request):
    return index_render(request, False)

def criar_usuario(request):
    form = NovoUsuarioForm()
    if request.method == 'POST':
        form = NovoUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, user)
            return index_render(request, True)
    return render(request, 'ecosite/criar_usuario.html', {
        'form':form
    })

def addprod(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    formprod = ProdutoForm()
    #empresa = Empresa.objects.get(nome=nome_empresa)
    empresa = Empresa.objects.get(proprietario=user)
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
            
def area_emp(request):
    empresa = Empresa.objects.get(proprietario=request.user)
    produtos = Produto.objects.filter(loja=empresa)
    return render(request, 'ecosite/area_empresa.html', {
        "empresa": empresa,
        "produtos": produtos,
        
    })

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return index_render(request, True)
        else:
            return render(request, 'ecosite/login.html', {
                'message': 'Credenciais invalidas'
            })
    return render(request, 'ecosite/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def criar_empresa(request):
    form = NovaEmpresaForm()
    if request.method == 'POST':
        form = NovoUsuarioForm(request.POST)
        if form.is_vaalid():
            obj = form.save()
            obj.proprietario = request.user
            return HttpResponseRedirect('')
        
    return render(request, 'ecosite/criar_empresa.html', {
        'form': form
    })