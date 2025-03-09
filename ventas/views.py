from django.shortcuts import render, redirect
from .forms import VentasForm
from django.http import JsonResponse
from .models import Ventas
from django.contrib import messages  
from .forms import VentasForm
from django.core.exceptions import ValidationError
from .forms import EliminarVentaForm


def agregar_venta(request):
    if request.method == 'POST':
        form = VentasForm(request.POST)
        if form.is_valid():
            try:
                # Guardar la venta
                form.save()
                messages.success(request, "Venta agregada con éxito.")  
                return redirect('lista_ventas') 
            except ValidationError as e:
                
                for error in e.messages:
                    messages.error(request, error)  
        else:
            messages.error(request, "Hay un error con el formulario. Verifique los campos.")
    else:
        form = VentasForm()

    return render(request, 'agregar_venta.html', {'form': form})

def lista_ventas(request):
    ventas = Ventas.objects.all().values('nro_factura', 'fecha', 'cuit', 'apellido', 'importe')
    return JsonResponse(list(ventas), safe=False)


def eliminar_venta(request):
    ventas = Ventas.objects.all()  # Obtener todas las ventas registradas

    if request.method == 'POST':
        form = EliminarVentaForm(request.POST)
        if form.is_valid():
            # Obtener los datos del formulario
            nro_factura = form.cleaned_data['nro_factura']
            cuit = form.cleaned_data['cuit']
            apellido = form.cleaned_data['apellido']

            try:
                
                venta = Ventas.objects.get(nro_factura=nro_factura, cuit=cuit, apellido=apellido)
                
                venta_details = f"Número de Factura: {venta.nro_factura}, CUIT: {venta.cuit}, Apellido: {venta.apellido}, Importe: {venta.importe}"
                
                venta.delete()
               
                messages.success(request, f"Venta eliminada con éxito. {venta_details}")
                ventas = Ventas.objects.all()  
            except Ventas.DoesNotExist:
                
                messages.error(request, "No se encontró la venta con los datos proporcionados.")
        else:
            messages.error(request, "Por favor, complete todos los campos correctamente.")
    else:
        form = EliminarVentaForm()

    return render(request, 'eliminar_venta.html', {'form': form, 'ventas': ventas})