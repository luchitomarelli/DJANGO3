from django.db import models
from proveedores.models import Proveedor
from django.core.exceptions import ValidationError

class Compra(models.Model):
    nro_factura = models.CharField(primary_key=True,max_length=30)
    fecha = models.DateField()
    razon_social = models.CharField(max_length=100)
    cuit = models.CharField(max_length=11)
    importe = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
   
        try:
            proveedor = Proveedor.objects.get(razon_social=self.razon_social, cuit=self.cuit)
        except Proveedor.DoesNotExist:
            raise ValidationError("No existe un proveedor con esa razón social y cuit.")
    
    def __str__(self):
        return f"Compra {self.nro_factura} - {self.razon_social}"
