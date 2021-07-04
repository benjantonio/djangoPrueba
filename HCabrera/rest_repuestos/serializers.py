from rest_framework import serializers
from productos.models import Repuesto


class RepuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repuesto
        fields = ['idRepuesto', 'nombreRepuesto', 'maquina','descripcionRepuesto']




