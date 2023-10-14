from django.contrib import admin
from django.urls import path, include
from facturacion.views.libros import *

urlpatterns = [
    path("libros/", render_index_libros, name="lista_libros"),
    path("libros/crear", crear_libro, name="crear_libro")
]