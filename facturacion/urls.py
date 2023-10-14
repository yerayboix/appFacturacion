from django.contrib import admin
from django.urls import path, include
from facturacion.views.libros import render_index_libros

urlpatterns = [
    path("libros/", render_index_libros, name="lista_libros")
]