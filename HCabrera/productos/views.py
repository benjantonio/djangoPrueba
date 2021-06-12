from django.shortcuts import render, redirect
from .models import Repuesto
from .forms import RepuestoForm

# FUNCION PARA LISTAR # 

def home(request):
    ListaRepuesto = Repuesto.objects.all()
    datos = {
        'Repuesto':ListaRepuesto,
    }

    return render(request, 'productos/index.html',datos)

#FUNCIÓN PARA INGRESAR PANEL ADMIN

def panel_admin(request):
    return render(request, 'productos/panel_admin.html')

# FUNCION PARA AGREGAR #

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



 # FUNCION PARA MODIFICAR #
def form_mod_repuesto(request, id):
    repuesto = Repuesto.objects.get(idRepuesto=id)

    datos = {
        'form': RepuestoForm(instance=repuesto)
    }
    if(request.method == 'POST'):
        formulario = RepuestoForm(data=request.POST, instance=repuesto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modificados correctamente'

    return render(request, 'productos/form_mod_repuesto.html', datos)

# FUNCION PARA ELIMINAR #

def form_del_repuesto(request, id):
    repuesto = Repuesto.objects.get(idRepuesto=id)
    repuesto.delete()

    return redirect(to='home')
