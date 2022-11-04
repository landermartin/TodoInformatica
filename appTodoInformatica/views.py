from django.shortcuts import render,get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Tienda,Categoria,Articulos,Provincia


# Create your views here.
def index_articulos(request):
    articulos= get_list_or_404(Articulos.objects.order_by('nombre'))
    output=', '.join([d.nombre for d in articulos])
    return HttpResponse(output)
    
    """context = {'lista_departamentos': articulos }
    return render(request, 'index.html', context)"""

def show_articulo(request,articulo_id):
    articulo = get_object_or_404(Articulos,pk=articulo_id)
    output = f'Detalles de la categoria: {articulo.id}, {articulo.nombre},{articulo.marca},{articulo.precio},{articulo.marca},{articulo.stock},{articulo.categoria},{articulo.vendedor}'
    return HttpResponse(output)

def index_categoria(request):
    categoria= get_list_or_404(Categoria.objects.order_by('nombre'))
    output=', '.join([d.nombre for d in categoria])
    return HttpResponse(output)

def show_categoria(request,categoria_id):
    categoria = get_object_or_404(Categoria,pk=categoria_id)
    output = f'Detalles de la categoria: {categoria.id}, {categoria.nombre}'
    return HttpResponse(output)

def index_Tiendas(request):
    tienda= get_list_or_404(Tienda.objects.order_by('nombre'))
    output=', '.join([d.nombre for d in tienda])
    return HttpResponse(output)

def show_Tiendas(request,tienda_id):
    tienda = get_object_or_404(Tienda,pk=tienda_id)
    output = f'Detalles de la articulo: {tienda.id}, {tienda.nombre},{tienda.direccion},{tienda.provincia}'
    return HttpResponse(output)
