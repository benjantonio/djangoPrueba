from django import forms
from django.forms import ModelForm
from .models import Repuesto


class RepuestoForm(ModelForm):
    class Meta:
        model = Repuesto
<<<<<<< HEAD
        fields = ['idRepuesto', 'nombreRepuesto', 'maquina']
=======
        fields = ['idRepuesto', 'nombreRepuesto', 'maquina','descripcionRepuesto']
>>>>>>> parent of f2cfc5d (Modificación html formulario)

