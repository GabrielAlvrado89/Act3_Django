from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("Empleados/", views.Empleados, name="Empleados"),
    path("Proveedores/", views.Proveedores, name="Proveedores"),
    path("Clientes/", views.Clientes, name="Clientes"),
    path("Sucursales/", views.Sucursales, name="Sucursales"),
]
