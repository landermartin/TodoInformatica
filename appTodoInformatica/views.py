from django.shortcuts import render,get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Tienda,Categoria,Articulos,Provincia


# Create your views here.
def index_main(request):
    return render(request,'index.hatml')

def index_categoria(request):
    categorias = get_list_or_404(Categoria.objects.order_by('nombre'))
    context = {'lista_categorias': categorias }
    return render(request, 'categorias.html', context)

def show_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    context = {'categoria': categoria }
    return render(request, 'categoria.html', context)

def index_articulos(request):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    articulos =  categoria.articulo_set.all()
    context = {'categoria': categoria, 'articulos' : articulos }
    return render(request, 'articulos.html', context)

def show_articulo(request,articulo_id):
    articulo = get_object_or_404(Articulos, pk=articulo_id)
    vendedor =  articulo.vendedor.all()
    context = { 'articulo': articulo, 'vendedor' : vendedor }
    return render(request, 'articulo.html', context)

def index_Tiendas(request):
    tiendas = get_list_or_404(Tienda.objects.order_by('nombre'))
    context = {'lista_tiendas': tiendas }
    return render(request, 'tiendas.html', context)

def show_Tienda(request,tienda_id):
    tienda = get_object_or_404(Tienda,pk=tienda_id)
    articulo =  tienda.articulo_set.all()
    context = { 'articulo': articulo, 'tienda' : tienda }
    return render(request, 'tienda.html', context)