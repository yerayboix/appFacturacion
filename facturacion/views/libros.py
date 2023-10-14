from django.shortcuts import render


def render_index_libros(request):
    return render(request, 'libros/index.html')