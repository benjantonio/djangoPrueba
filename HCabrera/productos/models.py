from django.db import models

 
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
 
   def __str__(self):

       return self.nombreRepuesto