from django.urls import path
from . import views

urlpatterns = [
 path('', views.index_articulos, name='index'),
 path('categoria/', views.index_categoria, name='categorias'),
 path('tienda/', views.index_Tiendas, name='tiendas'),
 path('tienda/<int:tienda_id>', views.show_Tiendas, name='tienda'),
 path('articulo/<int:articulo_id>', views.show_articulo, name='articulo'),
 path('categoria/<int:categoria_id>', views.show_categoria, name='categoria'),
]