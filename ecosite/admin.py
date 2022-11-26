from django.contrib import admin
from .models import Produto, Empresa, Imagem


# Register your models here.


admin.site.register(Empresa)
admin.site.register(Produto)
admin.site.register(Imagem)