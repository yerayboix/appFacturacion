from django.shortcuts import redirect, render
from django.contrib import messages
from django.db.models import F, ExpressionWrapper, fields
from facturacion.models import *


def render_index_libros(request):
    libros = Libro.objects.annotate(precio_iva=ExpressionWrapper(F('precio') * 1.04, output_field=fields.FloatField()))
    return render(request, 'libros/index.html', context={'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '')
        cantidad = request.POST.get('cantidad', '')
        precio = request.POST.get('precio', '')
        descuento = request.POST.get('descuento', '')
        try:
            nuevo_libro = Libro(
                titulo=titulo,
                cantidad=cantidad,
                precio=precio,
                descuento=descuento
            )
            nuevo_libro.save()
            messages.add_message(request, messages.SUCCESS, 'Libro añadido correctamente.')
        except Exception as e:
            messages.add_message(request, messages.ERROR, e)
    return redirect('/facturacion/libros')