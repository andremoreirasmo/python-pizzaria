from django.http import HttpResponse
from django.shortcuts import render
from Pizza.models import Pizza

def home(request):
    pizzas = Pizza.objects.all()
    return render(request, 'index.html', {'pizzas' : pizzas})

def areaRestrita(request):
    return render(request, 'index.html')