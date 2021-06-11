from django.shortcuts import render
from .models import Repuesto
from .forms import RepuestoForm

def home(request):
    ListaRepuesto = Repuesto.objects.all()
    datos = {
        'Repuesto':ListaRepuesto,
    }

    return render(request, 'productos/index.html',datos)


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
            datos['mensaje'] = 'ERROR. Ya exíste este ID..'
    return render(request,'productos/form_repuesto.html',datos) 

def form_mod_repuesto(request,id):
    repuesto = Repuesto.object.get(idRepuesto)
    datos = {
        'form': RepuestoForm(instance=repuesto)
    }
    return render(request,'core/form_mod_repuesto.html',datos)