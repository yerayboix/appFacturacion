from django.shortcuts import redirect, render
from django.contrib import messages
from cliente.models import *

def render_index_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/index.html', context={'clientes': clientes})

def crear_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        nif = request.POST.get('nif', '')
        domicilio = request.POST.get('domicilio', '')
        ciudad = request.POST.get('ciudad', '')
        cp = request.POST.get('cp', '')
        telefono = request.POST.get('telefono', '')
        tipo = request.POST.get('tipo', '')
        try:
            nuevo_cliente = Cliente(
                nombre=nombre,
                nif=nif,
                domicilio=domicilio,
                ciudad=ciudad,
                cp=cp,
                telefono=telefono,
                tipo=tipo
            )
            nuevo_cliente.save()
            messages.add_message(request, messages.SUCCESS, 'Cliente añadido correctamente.')
        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR, e)
        
    return redirect('/clientes')

def editar_cliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == 'POST':
        nombre = request.POST.get('nombre_editar', '')
        nif = request.POST.get('nif_editar', '')
        domicilio = request.POST.get('domicilio_editar', '')
        ciudad = request.POST.get('ciudad_editar', '')
        cp = request.POST.get('cp_editar', '')
        telefono = request.POST.get('telefono_editar', '')
        tipo = request.POST.get('tipo_editar', '')
        try:
            cliente.nombre = nombre
            cliente.nif = nif
            cliente.domicilio = domicilio
            cliente.ciudad = ciudad
            cliente.cp = cp
            cliente.telefono = telefono
            cliente.tipo = tipo
            cliente.save()
            messages.add_message(request, messages.SUCCESS, 'Cliente editado correctamente.')
        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR, e)
    return redirect('/clientes')

def borrar_cliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    try:
        cliente.delete()
        messages.add_message(request, messages.SUCCESS, 'Cliente borrado correctamente.')
    except Exception as e:
        print(e)
        messages.add_message(request, messages.ERROR, e)
    return redirect('/clientes')