from django.urls import path
from rest_repuestos.views import lista_repuestos, detalle_repuestos

urlpatterns = [
    path('lista-repuestos',lista_repuestos,name='lista_repuestos'),
    path('detalle-repuestos/<id>',detalle_repuestos,name='detalle_repuestos'),
]