from django.urls import include, path
from . import views

urlpatterns = [
 path('', views.index_main, name='index'),
 path('articulo/',views.index_articulos,name='articulos'),
 path('categoria/', views.index_categoria, name='categorias'),
 path('tienda/', views.index_tiendas, name='tiendas'),
 path('tienda/<int:tienda_id>', views.show_tienda, name='tienda'),
 path('articulo/<int:articulo_id>', views.show_articulo, name='articulo'),
 path('categoria/<int:categoria_id>', views.show_categoria, name='categoria'),
 path('articuloTienda/', views.index_articulosTienda, name='articulosTienda'),
 path('articuloCategoria/', views.index_articulosCategoria, name='articulosCategoria'),
 path('troll/', views.troll, name='troll'),
 path("__reload__/", include("django_browser_reload.urls")),
]