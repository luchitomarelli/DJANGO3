
from django import forms
from .models import Ventas

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = ['nro_factura', 'fecha', 'cuit', 'apellido', 'importe']


class EliminarVentaForm(forms.Form):
    nro_factura = forms.CharField(max_length=20)
    cuit = forms.CharField(max_length=11)
    apellido = forms.CharField(max_length=200)
