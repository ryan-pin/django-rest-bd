from rest_framework import serializers
from .models import Cliente
from .models import Endereço

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__' 

class EndereçoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereço
        fields = '__all__' 