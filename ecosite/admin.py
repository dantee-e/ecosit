from django.contrib import admin
from .models import Usuario, Produto, Empresa, Imagem


# Register your models here.
class EmpresaAdmin(admin.ModelAdmin):
	list_display = ('id', 'nome', 'telefone')

class ProdutoAdmin(admin.ModelAdmin):
	folter_horizontal = ('imagem', )


admin.site.register(Usuario)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Imagem)