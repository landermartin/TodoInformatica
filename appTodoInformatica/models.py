from django.db import models

# Create your models here.

class Provincia(models.Model):
    nombre=models.CharField(max_length=50) 

    def __str__(self):
        return self.nombre


class Tienda(models.Model):
    nombre = models.CharField(max_length=60) 
    direccion=models.CharField(max_length=70) 
    provincia=models.ForeignKey(Provincia, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre=models.CharField(max_length=60) 

    def __str__(self):
        return self.nombre



class Articulos(models.Model):
    nombre = models.CharField(max_length=60)
    marca=models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.BooleanField()
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    vendedor=models.ManyToManyField(Tienda)

    def __str__(self):
        return self.nombre
