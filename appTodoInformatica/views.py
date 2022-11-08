from django.shortcuts import render,get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Tienda,Categoria,Articulos,Provincia


# Create your views here.
def index_main(request):
    return render(request,'index.html')

def index_categoria(request):
    categorias = get_list_or_404(Categoria.objects.order_by('nombre'))
    context = {'lista_categorias': categorias }
    return render(request, 'categorias.html', context)

def show_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    articulos = get_list_or_404(Articulos.objects.order_by('nombre'))
    context = {'categoria': categoria, 'articulos': articulos }
    return render(request, 'categoria.html', context)

def index_articulos(request):
    articulos = get_list_or_404(Articulos.objects.order_by('nombre'))
    context = {'articulos': articulos}
    return render(request, 'articulos.html', context)

def index_articulosTienda(request, tienda_id):
    tienda = get_object_or_404(Tienda, pk=tienda_id)
    articulos = tienda.articulo_set.all()
    context = {'tienda': tienda,'articulos': articulos}
    return render(request, 'articulos.html', context)

def index_articulosCategoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    articulos = categoria.articulo_set.all()
    context = {'categoria': categoria,'articulos': articulos}
    return render(request, 'articulos.html', context)

def show_articulo(request,articulo_id):
    articulo = get_object_or_404(Articulos, pk=articulo_id)
    context = { 'articulo': articulo, 'vendedor': articulo.vendedor.all}
    return render(request, 'articulo.html', context)

def index_tiendas(request):
    tiendas = get_list_or_404(Tienda.objects.order_by('nombre'))
    context = {'tiendas': tiendas }
    return render(request, 'tiendas.html', context)

def show_tienda(request,tienda_id):
    tienda = get_object_or_404(Tienda,pk=tienda_id)
    articulos = get_list_or_404(Articulos.objects.order_by('nombre'))
    context = {'tienda' : tienda, 'articulos': articulos}
    return render(request, 'tienda.html', context)