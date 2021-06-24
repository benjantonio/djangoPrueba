from django.urls import path
from rest_repuestos.views import lista_repuestos

urlpatterns = [
    path('lista_repuestos',lista_repuestos,name='lista_repuestos'),
]