from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    codigo_producto = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
