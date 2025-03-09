from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CompraForm
from .models import Compra
from django.http import JsonResponse



def agregar_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, "Compra agregada exitosamente.")
            return redirect('lista_compras')  
        else:
            messages.error(request, "Hubo un error al agregar la compra.")
    else:
        form = CompraForm()

    return render(request, 'agregar_compra.html', {'form': form})



def lista_compras(request):
    compras = Compra.objects.all()
    return render(request, 'lista_compras.html', {'compras': compras})



def lista_compras_json(request):
    compras = Compra.objects.all().values('nro_factura', 'fecha', 'razon_social', 'cuit', 'importe')
    return JsonResponse(list(compras), safe=False)




def eliminar_compra(request):
    if request.method == 'POST':
        nro_factura = request.POST.get('nro_factura')
        razon_social = request.POST.get('razon_social')
        cuit = request.POST.get('cuit')

        try:
            
            compra = Compra.objects.get(nro_factura=nro_factura, razon_social=razon_social, cuit=cuit)
            
            compra.delete()
            messages.success(request, f"La compra con factura {nro_factura} ha sido eliminada.")
        except Compra.DoesNotExist:
           
            messages.error(request, "No se encontró una compra con esos datos. Verifique los valores ingresados.")

        return redirect('eliminar_compra')  

    
    compras = Compra.objects.all()  
    return render(request, 'eliminar_compra.html', {'compras': compras})