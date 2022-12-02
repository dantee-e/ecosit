from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.



class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, celular, **extra_fields):
        if not email:
            raise ValueError('Email must be provided')
        if not password:
            raise ValueError('Password must be provided')
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            celular = celular,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password, first_name, last_name, celular, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, first_name, last_name, celular, **extra_fields)



    def create_superuser(self, email, password, first_name, last_name, celular, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, first_name, last_name, celular, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50,unique=True)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=255)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    is_proprietario = models.BooleanField(default=False)
    celular = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30, blank=True)
    

    objects = CustomUserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','celular']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Empresa(models.Model):
    proprietario = models.ForeignKey(Usuario, related_name='empresa', on_delete=models.CASCADE)
    CNPJ = models.CharField(max_length=20)
    nome = models.CharField(max_length=60)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    def __str__(self):
        return f"Loja: {self.nome}"
    
class Endereco_empresa(models.Model):
    empresa = models.ForeignKey(Empresa, related_name='endereco_empresa', on_delete=models.CASCADE)
    CEP = models.CharField(max_length=10)
    estado = models.CharField(max_length=3)
    cidade = models.CharField(max_length=35)
    endereco_logradouro = models.CharField(max_length=70)
    def __str__(self):
        return f'{self.estado} - {self.cidade} - {self.endereco_logradouro}'

class Endereco_comprador(models.Model):
    usuario = models.ForeignKey(Empresa, related_name='endereco_compra', on_delete=models.CASCADE)
    CEP = models.CharField(max_length=10)
    estado = models.CharField(max_length=3)
    cidade = models.CharField(max_length=35)
    endereco_logradouro = models.CharField(max_length=70)
    def __str__(self):
        return f'{self.estado} - {self.cidade} - {self.endereco_logradouro}'

class Produto(models.Model):
    loja = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="produto")
    nome = models.CharField(max_length=60)
    preco = models.FloatField()
    home = models.BooleanField(default=1)
    descricao = models.CharField(max_length=300)
    qnt_compra_max = models.IntegerField()
    quantidade_estoque = models.IntegerField()
    def __str__(self):
        return f"{self.nome} da {self.loja}"

class Imagem(models.Model):
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="imagem")
    def __str__(self):
        return f"Imagem do produto {self.produto}"

