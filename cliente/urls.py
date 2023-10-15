from django.contrib import admin
from django.urls import path, include
from cliente.views.clientes import *

urlpatterns = [
    path("", render_index_clientes, name="lista_clientes"),
    path("crear/", crear_cliente, name="crear_cliente"),
    path("editar/<pk>", editar_cliente, name="editar_cliente"),
    path("borrar/<pk>", borrar_cliente, name="borrar_cliente"),
]