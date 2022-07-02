from django.db import models
import os
import datetime

###################################################################
#--------------------model exterior-----------------------------
###################################################################

class Revision(models.Model):
    fecha= models.DateTimeField(blank=True, auto_now_add=True, auto_now=False)
    nombre=models.CharField(max_length=255, blank=True,default="No registrado")
    class Meta:
        verbose_name = 'Datos'
        verbose_name_plural = 'Revisiones' 
    def __str__(self):
        return f'{self.fecha.strftime("%d/%m/%Y , %H:%M:%S")} || {self.nombre}'

class Add_data(models.Model):
    fecha= models.DateTimeField(blank=True, auto_now_add=True, auto_now=False)
    nombre=models.CharField(max_length=255, blank=True,default="No registrado")
    local= models.CharField(max_length=255, blank=True,default="No registrado")
    clima= models.CharField(max_length=255, blank=True,default="No registrado")
    t_ext= models.FloatField(blank=True,default=0)
    t_int= models.FloatField(blank=True,default=0)
    humedad= models.FloatField(blank=True,default=0)
    peso= models.FloatField(blank=True,default=0)
    comida= models.FloatField(blank=True,default=0)
    piquera=  models.CharField(max_length=255,blank=True,default="Cerrada")
    id_revision = models.ForeignKey(Revision, null=True, on_delete=models.SET_NULL)
    class Meta:
        verbose_name = 'Datos'
        verbose_name_plural = 'Colmenas Supervisadas' 
    def __str__(self):
        return f'{self.fecha.strftime("%d/%m/%Y , %H:%M:%S")} || {self.local} , {self.nombre}'


class No_revisado(models.Model):
    fecha= models.DateTimeField(blank=True, auto_now_add=True, auto_now=False)
    nombre=models.CharField(max_length=255, blank=True,default="No registrado")
    local= models.CharField(max_length=255, blank=True,default="No registrado")
    t_int= models.FloatField(blank=True,default=0)
    class Meta:
        verbose_name = 'Datos'
        verbose_name_plural = 'Colmenas no Supervisadas' 
    def __str__(self):
        return f'{self.fecha.strftime("%d/%m/%Y , %H:%M:%S")} || {self.local} , {self.nombre}'

class Errors(models.Model):
    fecha= models.DateTimeField(blank=True, auto_now_add=True, auto_now=False)
    error=models.CharField(max_length=255, blank=True,default="No registrado")
    class Meta:
        verbose_name = 'Errores'
        verbose_name_plural = 'Historial_de_errores' 
    def __str__(self):
        return f'{self.fecha.strftime("%d/%m/%Y , %H:%M:%S")} '


        

