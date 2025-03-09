
from django.db import models

class Proveedor(models.Model):
    razon_social = models.CharField(max_length=200)
    cuit = models.CharField(max_length=11, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre