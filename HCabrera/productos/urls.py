from django.urls import path
from .views import form_maquina, home

urlpatterns = [
    path('',home,name='home'),
    path('form-maquina',form_maquina,name='form_maquina'),
]