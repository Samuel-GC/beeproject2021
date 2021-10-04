from django.db import models
import os


###################################################################
#--------------------model exterior-----------------------------
###################################################################

class Add_data(models.Model):
    fecha= models.DateTimeField(blank=True, auto_now_add=True, auto_now=False)
    nombre=models.CharField(max_length=255, blank=True,default="No registrado")
    local= models.CharField(max_length=255, blank=True,default="No registrado")
    clima= models.CharField(max_length=255, blank=True,default="No registrado")
    t_Ext= models.FloatField(blank=True,default=0)
    t_int= models.FloatField(blank=True,default=0)
    humedad= models.FloatField(blank=True,default=0)
    peso= models.FloatField(blank=True,default=0)
    comida= models.FloatField(blank=True,default=0)
    piquera=  models.CharField(max_length=255,blank=True,default="Cerrada")
    revision= models.DateTimeField(blank=True, auto_now_add=False, auto_now=True)
    class Meta:
        verbose_name = 'Datos'
        verbose_name_plural = 'Colmenas_supervisadas' 
    def __str__(self):
        return f'{self.fecha} {self.local} {self.nombre}'

class No_revisado(models.Model):
    fecha= models.DateTimeField(blank=True, auto_now_add=True, auto_now=False)
    nombre=models.CharField(max_length=255, blank=True,default="No registrado")
    local= models.CharField(max_length=255, blank=True,default="No registrado")
    t_int= models.FloatField(blank=True,default=0)
    class Meta:
        verbose_name = 'Datos'
        verbose_name_plural = 'Colmenas_no_supervisadas' 
    def __str__(self):
        return f'{self.fecha} {self.local} {self.nombre}'

class Errors(models.Model):
    fecha= models.DateTimeField(blank=True, auto_now_add=True, auto_now=False)
    error=models.CharField(max_length=255, blank=True,default="No registrado")
    class Meta:
        verbose_name = 'Errores'
        verbose_name_plural = 'Historial_de_errores' 
    def __str__(self):
        return f'{self.fecha} '