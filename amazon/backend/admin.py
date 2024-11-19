from django.contrib import admin
# from .models import Cliente
from .models import *

admin.site.register(Cliente)
admin.site.register(Endereço)
admin.site.register(Perfil)
admin.site.register(Item)
admin.site.register(FormaPagamento) 
admin.site.register(Pedido)
admin.site.register(Vendedor)