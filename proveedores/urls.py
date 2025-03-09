from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('lista/', views.lista_proveedores, name='lista_proveedores'),
    path('eliminar/', views.eliminar_proveedor, name='eliminar_proveedor'),
]