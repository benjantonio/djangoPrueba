from django import forms
from django.forms import ModelForm
from .models import Maquina


class MaquinaForm(ModelForm):
    class Meta:
        model = Maquina
        fields = ['idMaquina', 'marcaMaquina', 'modeloMaquina']

