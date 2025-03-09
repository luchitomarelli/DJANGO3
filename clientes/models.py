from django.db import models

class Cliente(models.Model):
    cuit = models.CharField(primary_key=True, max_length=11)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)  

    def __str__(self):
        return f'{self.nombre} {self.apellido}'