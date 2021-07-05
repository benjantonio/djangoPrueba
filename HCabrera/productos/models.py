from django.db import models
from django.utils.translation import ugettext as _

 
# Create your models here.

class Maquina(models.Model):
   idMaquina = models.IntegerField(primary_key=True,verbose_name='Id de maquina')
   marcaMaquina = models.CharField(max_length=50,verbose_name='Nombre de la maquina')
   modeloMaquina = models.CharField(max_length=50,verbose_name='Modelo de la maquina')

   def __str__(self):
       return self.marcaMaquina

class Repuesto(models.Model):
    idRepuesto = models.IntegerField(primary_key=True,verbose_name='Id de repuesto')
    nombreRepuesto = models.CharField(max_length=20, verbose_name='Nombre repuesto')
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    descripcionRepuesto = models.CharField(max_length=300, verbose_name='Descripción repuesto')
 
    def __str__(self):
        return self.nombreRepuesto

    class Meta:
        permissions = (
            ('admin',_('Es administrador')),
            ('cliente',_('Es cliente')),
            )

class Servicio(models.Model):
    idServicio = models.IntegerField(primary_key=True,verbose_name='Id de servicio')
    nombreServicio = models.CharField(max_length=25, verbose_name='Nombre servicio')
    descripcionServicio = models.CharField(max_length=120, verbose_name='Descripcion servicio')
 
    def __str__(self):

       return self.nombreServicio

       