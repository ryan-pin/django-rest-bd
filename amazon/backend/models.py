from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f'{self.nome} - {self.email}'
    
class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f'{self.nome} - {self.email}'
    
class Endereço(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    rua = models.CharField(max_length=200)
    cep = models.CharField(max_length=200)
    numero = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.nome} - {self.rua} - {self.numero} - {self.cep}'
    
class Perfil(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos/')
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=1, choices=(('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')))
    cpf = models.CharField(max_length=14)
    tipo = models.CharField(max_length=1, choices=(('F', 'Física'), ('J', 'Jurídica')))

    def __str__(self):
        return f'{self.cliente.nome} - {self.genero} - {self.data_nascimento}'
    
class Item (models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.IntegerField()
    
    def __str__(self):
        return f'{self.nome} - {self.descricao} - R$ {self.preco} - Estoque: {self.estoque}'

class FormaPagamento(models.Model):
    descricao = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descricao

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    endereco_entrega = models.ForeignKey(Endereço, on_delete=models.CASCADE)
    itens = models.ManyToManyField(Item)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateTimeField()
    itens = models.ManyToManyField(Item)
    
    def __str__(self): 
        return f'{self.cliente} - {self.vendedor} - {self.data_pedido}'