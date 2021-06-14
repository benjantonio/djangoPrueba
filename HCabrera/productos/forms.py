from django import forms
from django.forms import ModelForm
from .models import Repuesto


class RepuestoForm(ModelForm):
    class Meta:
        model = Repuesto
        fields = ['idRepuesto', 'nombreRepuesto', 'maquina','descripcionRepuesto']




