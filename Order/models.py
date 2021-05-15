from django.db import models
from Pizza.models import Pizza
from clientes.models import Client

# Create your models here.
class Order(models.Model):
    pizzas = models.ManyToManyField(Pizza)
    clients = models.ManyToManyField(Client)
    amount = models.IntegerField(null=False)
    value = models.FloatField(null=False)
    status = models.CharField(
        max_length=1, default='P', help_text='P - Pendente, F - Finalizado')

    def __str__(self):
        return 'Pedido'
