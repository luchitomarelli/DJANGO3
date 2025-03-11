from django.shortcuts import render, redirect
from .forms import ProveedorForm
from django.http import JsonResponse
from .models import Proveedor
from django.contrib import messages

def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')  
    else:
        form = ProveedorForm()
        return render(request, 'agregar_proveedor.html', {'form': form})

def lista_proveedores(request):
    proveedores = Proveedor.objects.all().values('razon_social', 'cuit', 'direccion','telefono','email')
    return JsonResponse(list(proveedores), safe=False)

def eliminar_proveedor(request):
     proveedores = Proveedor.objects.all()
     if request.method == 'POST':
        cuit = request.POST.get('cuit')
        razon_social = request.POST.get('razon_social')
        proveedor = Proveedor.objects.filter(cuit=cuit, razon_social=razon_social).first()

        if proveedor:
            proveedor.delete()
            messages.success(request, f"Proveedor {razon_social} con CUIT {cuit} eliminado correctamente.")
            return redirect('eliminar_proveedor')  
        else:
            messages.error(request, "No existe un proveedor con el CUIT y Razón Social proporcionados.")
            return render(request, 'eliminar_proveedor.html', {'proveedores': proveedores})
