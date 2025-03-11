from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Cliente
from .forms import ClienteForm

def home(request):
    return render(request, 'home.html')

def lista_clientes(request):
    clientes = Cliente.objects.all().values('cuit', 'nombre', 'apellido', 'telefono', 'email')
    return JsonResponse(list(clientes), safe=False)

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')  
    else:
        form = ClienteForm()
    return render(request, 'agregar_cliente.html', {'form': form})

def eliminar_cliente(request):
    if request.method == 'POST':
        cuit = request.POST.get('cuit')
        apellido = request.POST.get('apellido')

        try:
            
            cliente = Cliente.objects.get(cuit=cuit, apellido=apellido)
            cliente.delete()

            
            messages.success(request, f'Cliente {cliente.nombre} {cliente.apellido} con CUIT {cliente.cuit} ha sido eliminado con éxito.')

            
            return redirect('home')

        except Cliente.DoesNotExist:
            messages.error(request, 'No se encontró un cliente con esos datos.')
            return redirect('home')  

    return render(request, 'eliminar_cliente.html')