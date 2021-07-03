from django.db import models
import os


###################################################################
#--------------------model exterior-----------------------------
###################################################################

class Add_data(models.Model):
    fecha= models.DateTimeField(blank=True, auto_now_add=True, auto_now=False)
    nombre=models.CharField(max_length=255, blank=True,default="No registrado")
    ubicacion= models.CharField(max_length=255, blank=True,default="No registrado")
    clima= models.CharField(max_length=255, blank=True,default="No registrado")
    temp_Ext= models.FloatField(blank=True,default=0)
    temp_int= models.FloatField(blank=True,default=0)
    humedad_int= models.FloatField(blank=True,default=0)
    peso_colmena= models.FloatField(blank=True,default=0)
    poblacion= models.FloatField(blank=True,default=0)
    comida= models.FloatField(blank=True,default=0)
    piquera=  models.CharField(max_length=255,blank=True,default="Cerrada")
    reina= models.CharField(max_length=255,blank=True,default="Adentro")
    revision= models.CharField(max_length=255,blank=True,default="No revisado")

    def __str__(self):
        return f'{self.fecha} {self.ubicacion} {self.nombre}'

class No_revisado(models.Model):
    fecha= models.DateTimeField(blank=True, auto_now_add=True, auto_now=False)
    nombre=models.CharField(max_length=255, blank=True,default="No registrado")
    ubicacion= models.CharField(max_length=255, blank=True,default="No registrado")
    temp_int= models.FloatField(blank=True,default=0)

    def __str__(self):
        return f'{self.fecha} {self.ubicacion} {self.nombre}'
