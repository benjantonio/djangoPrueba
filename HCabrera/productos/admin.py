from django.contrib import admin
from .models import Maquina
from .models import Repuesto

# Register your models here.

admin.site.register(Maquina)
admin.site.register(Repuesto)
