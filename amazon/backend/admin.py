from django.contrib import admin
from .models import Cliente
from .models import Endereço

admin.site.register(Cliente)
admin.site.register(Endereço)