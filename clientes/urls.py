from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista_clientes/', views.lista_clientes, name='lista_clientes'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('eliminar_cliente/', views.eliminar_cliente, name='eliminar_cliente'),  
]