from django.shortcuts import render
from .models import Repuesto
from .forms import RepuestoForm
import logging
logger = logging.getLogger(__name__)

#Listar
def home(request):
    ListaRepuesto = Repuesto.objects.all()
    datos = {
        'Repuesto':ListaRepuesto,
    }

    return render(request, 'productos/index.html',datos)

#Agregar
def form_repuesto(request):
    datos = {
        'form':RepuestoForm()
    }
    

    if(request.method == 'POST'):
        formulario = RepuestoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardado Correctamente'
        else:
            datos['mensaje'] = '¡ERROR! Ya exíste el ID'
    return render(request,'productos/form_repuesto.html',datos)


def form_mod_repuesto(request, id):
    repuesto = Repuesto.objects.get(idRepuesto=id)

    datos = {
        'form': RepuestoForm(instance=repuesto)
    }

    return render(request, 'productos/form_mod_repuesto.html', datos)
