from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_venta, name='agregar_venta'),
    path('lista/', views.lista_ventas, name='lista_ventas'),
    path('eliminar/', views.eliminar_venta, name='eliminar_venta'),
    
]