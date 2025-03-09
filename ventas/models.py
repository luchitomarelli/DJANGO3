from django.core.exceptions import ValidationError
from django.db import models
from clientes.models import Cliente

class Ventas(models.Model):
    nro_factura = models.CharField(max_length=20, primary_key=True)
    fecha = models.DateField()
    cuit = models.CharField(max_length=11)
    apellido = models.CharField(max_length=200)
    importe = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        
        if not Cliente.objects.filter(cuit=self.cuit, apellido=self.apellido).exists():
            raise ValidationError("No existe CUIT relacionado con ese Apellido en la base de datos.")

    def save(self, *args, **kwargs):
        self.clean()  
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Factura {self.nro_factura} - {self.fecha} - {self.cuit} - {self.apellido}"