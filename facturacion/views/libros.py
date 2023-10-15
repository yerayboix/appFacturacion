from django.shortcuts import redirect, render
from django.contrib import messages
from django.db.models import F, ExpressionWrapper, FloatField, Func
from facturacion.models import *


def render_index_libros(request):
    libros = Libro.objects.annotate(precio_iva=ExpressionWrapper(Func(F('precio') * 1.04, function='ROUND', template='%(function)s(%(expressions)s, 2)'), output_field=FloatField()))
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
            print(e)
            messages.add_message(request, messages.ERROR, e)
    return redirect('/facturacion/libros')

def editar_libro(request, pk):
    libro = Libro.objects.get(id=pk)
    if request.method == 'POST':
        titulo = request.POST.get('titulo_editar', '')
        cantidad = request.POST.get('cantidad_editar', '')
        precio = request.POST.get('precio_editar', '')
        descuento = request.POST.get('descuento_editar', '')
        try:
            libro.titulo = titulo
            libro.cantidad = cantidad
            libro.precio = precio
            libro.descuento = descuento
            libro.save()
            messages.add_message(request, messages.SUCCESS, 'Libro editado correctamente.')
        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR, e)
    return redirect('/facturacion/libros')

def borrar_libro(request, pk):
    libro = Libro.objects.get(id=pk)
    try:
        libro.delete()
        messages.add_message(request, messages.SUCCESS, 'Libro borrado correctamente.')
    except Exception as e:
        print(e)
        messages.add_message(request, messages.ERROR, e)
    return redirect('/facturacion/libros')