from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_compra, name='agregar_compra'),
    path('lista/', views.lista_compras, name='lista_compras'), 
    path('lista_json/', views.lista_compras_json, name='lista_compras_json'),
    path('eliminar/', views.eliminar_compra, name='eliminar_compra'),
]