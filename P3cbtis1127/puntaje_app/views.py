from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def Empleados(request):
    return render(request, 'Empleados.html')

def Clientes(request):
    return render(request, 'Clientes.html')

def Proveedores(request):
    return render(request, 'Proveedores.html')

def Sucursales(request):
    return render(request, 'Sucursales.html')