from django.db import models

# Create your models here.


class Pizza(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text='Nome')
    value = models.FloatField(null=False, help_text='Valor')
    length = models.CharField(
        max_length=1, default='P', help_text='P - Pequena, M - Média, G - Grande')
    detail = models.CharField(
        max_length=500, help_text='Sabor ou qualquer outra informação.', null=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100, null=False, help_text='Nome')
    telephone = models.CharField(
        max_length=50, null=False, help_text='Telefone')
    address = models.CharField(
        max_length=300, null=False, help_text='Endereço')
    email = models.CharField(max_length=150, null=True, help_text='Email')

    def __str__(self):
        return self.name


class Order(models.Model):
    pizzas = models.ManyToManyField(Pizza)
    clients = models.ManyToManyField(Client)
    amount = models.IntegerField(null=False)
    value = models.FloatField(null=False)
    status = models.CharField(
        max_length=1, default='P', help_text='P - Pendente, F - Finalizado')

    def __str__(self):
        return 'Pedido'
