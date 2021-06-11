from django.contrib import admin
from .models import Maquina
from .models import Repuesto
from .models import Servicio

# Register your models here.

admin.site.register(Maquina)
admin.site.register(Repuesto)
admin.site.register(Servicio)