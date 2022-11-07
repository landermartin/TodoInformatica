from django.urls import path
from . import views

urlpatterns = [
 path('', views.index_main, name='index'),
 path('articulo/',views.index_articulos,name='articulos'),
 path('categoria/', views.index_categoria, name='categorias'),
 path('tienda/', views.index_Tiendas, name='tienda'),
 path('tienda/<int:tienda_id>', views.show_Tienda, name='tienda'),
 path('articulo/<int:articulo_id>', views.show_articulo, name='articulo'),
 path('categoria/<int:categoria_id>', views.show_categoria, name='categoria'),
]