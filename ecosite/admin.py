from django.contrib import admin
from .models import Produto, Empresa


# Register your models here.


admin.site.register(Empresa)
admin.site.register(Produto)