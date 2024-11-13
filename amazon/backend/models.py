from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f'{self.nome} - {self.email}'
    
class Endereço(models.Model):
    nome = models.CharField(max_length=100)
    rua = models.CharField(max_length=200)
    cep = models.CharField(max_length=200)
    numero = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.nome} - {self.rua} - {self.numero} - {self.cep}'