from django.shortcuts import render
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
    return render(request,'productos/form_repuesto.html',datos)


def form_mod_repuesto(request, id):
    repuesto = Repuesto.objects.get(idRepuesto=id)

    datos = {
        'form': RepuestoForm(instance=repuesto)
    }

    return render(request, 'productos/form_mod_repuesto.html', datos)
=======

def home(request):
    return render(request, 'productos/index.html')
>>>>>>> parent of b967b03 (Incorporación form)
=======

def home(request):
    return render(request, 'productos/index.html')
>>>>>>> parent of b967b03 (Incorporación form)
=======

def home(request):
    return render(request, 'productos/index.html')
>>>>>>> parent of b967b03 (Incorporación form)
=======
    return render(request,'productos/form_repuesto.html',datos)
>>>>>>> parent of 8a155c2 (Modificación diseño tabla y creación mod_form)
=======
    return render(request,'productos/form_repuesto.html',datos) 

def form_mod_repuesto(request,id):
    repuesto = Repuesto.object.get(idRepuesto)
    datos = {
        'form': RepuestoForm(instance=repuesto)
    }
    return render(request,'core/form_mod_repuesto.html',datos)
>>>>>>> parent of f2cfc5d (Modificación html formulario)
