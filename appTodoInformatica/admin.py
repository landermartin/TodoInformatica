from django.contrib import admin
from .models import Tienda, Articulos, Provincia,Categoria


# Register your models here.
admin.site.register(Tienda)
admin.site.register(Articulos)
admin.site.register(Provincia)
admin.site.register(Categoria)