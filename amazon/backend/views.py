from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer

from .models import Endereço
from .serializers import EndereçoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer 

class EndereçoViewSet(viewsets.ModelViewSet):
    queryset = Endereço.objects.all()
    serializer_class = EndereçoSerializer 
