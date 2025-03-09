from django.shortcuts import render, redirect 
from django.http import JsonResponse
from .models import Producto
from .forms import ProductoForm
from django.contrib import messages



def lista_productos(request):
   
    productos = Producto.objects.all().values('nombre', 'descripcion', 'precio', 'stock', 'codigo_producto')
  
    return JsonResponse(list(productos), safe=False)

from django.shortcuts import render, redirect
from .forms import ProductoForm




def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos') 
    else:
        form = ProductoForm()

    return render(request, 'agregar_producto.html', {'form': form})




def eliminar_producto(request):
    if request.method == 'POST':
        codigo_producto = request.POST.get('codigo_producto')  

        try:
            
            producto = Producto.objects.get(codigo_producto=codigo_producto)
            producto_data = {
                'nombre': producto.nombre,
                'descripcion': producto.descripcion,
                'precio': producto.precio,
                'stock': producto.stock,
                'codigo_producto': producto.codigo_producto,
            }
            
            producto.delete()
            messages.success(request, f"Producto eliminado con éxito: {producto_data}")
        except Producto.DoesNotExist:
            
            messages.error(request, "No se encontró el producto con ese código.")
    
    return render(request, 'eliminar_producto.html')

