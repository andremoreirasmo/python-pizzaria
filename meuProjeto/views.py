from django.http import HttpResponse
from django.shortcuts import render
from Pizza.models import Pizza
from clientes.models import Client
from Order.models import Order

def home(request):
    pizzas = Pizza.objects.all()
    return render(request, 'index.html', {'pizzas' : pizzas})

def areaRestrita(request):
    pizzas = Pizza.objects.all()
    orders = Order.objects.all()
    clients = Client.objects.all()
    return render(request, 'index_areaRestrita.html', {'pizzas' : pizzas, 'orders': orders, 'clients': clients})