# clientes_app/forms.py
from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'cuit', 'telefono', 'email']

class EliminarClienteForm(forms.Form):
    apellido = forms.CharField(max_length=100)
    cuit = forms.CharField(max_length=13)  
