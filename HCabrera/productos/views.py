from django.shortcuts import render
from .models import Maquina
from .forms import MaquinaForm

def home(request):
    ListaMaquina = Maquina.objects.all()
    datos = {
        'maquinas':ListaMaquina,
    }

    return render(request, 'productos/index.html',datos)


def form_maquina(request):
    datos = {
        'form':MaquinaForm()
    }

    if(request.method == 'POST'):
        formulario = MaquinaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardado Correctamente'
        else:
            datos['mensaje'] = 'ERROR. Ya exíste este ID..'
    return render(request,'productos/form_maquina.html',datos)