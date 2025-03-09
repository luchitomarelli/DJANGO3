from django import forms
from .models import Compra
from proveedores.models import Proveedor

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['nro_factura', 'fecha', 'razon_social', 'cuit', 'importe']

    def clean(self):
        cleaned_data = super().clean()
        cuit = cleaned_data.get('cuit')
        razon_social = cleaned_data.get('razon_social')
        
        
        if not Proveedor.objects.filter(cuit=cuit, razon_social=razon_social).exists():
            raise forms.ValidationError("El CUIT y la Razón Social no coinciden con ningún proveedor registrado.")
        
        return cleaned_data
