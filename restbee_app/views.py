from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import generics
from restbee_app.models import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import *
from rest_framework.response import Response
from django.shortcuts import redirect # libreria para redireccionar paginas
from django.shortcuts import render #libreria para activar las paginas
from django.template import Template #libreria para mostrar los template y enviar contextos a los html
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.utils.timezone import now
from django.utils import timezone
import datetime
import pathlib
import gspread
from oauth2client.service_account import ServiceAccountCredentials
###########################################################
#-----------------------Rest APP---------------------------
###########################################################



class agregar_data(APIView):  # READY

	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]
	def post(self, request, *args, **kwargs):
		try:
			nombre = request.data.get("nombre")
			local = request.data.get("local")
			clima = request.data.get("clima")
			exterior = float(request.data.get("t_ext"))
			exterior=round(exterior,2)
			interior = float(request.data.get("t_int"))
			interior=round(interior,2)
			humedad = float(request.data.get("humedad"))
			humedad=round(humedad,2)
			peso = float(request.data.get("peso"))
			peso=round(peso,2)
			comida = float(request.data.get("comida"))
			comida=round(comida,1)
			if comida <=0:
			    comida=0
			piquera = request.data.get("piquera")

			dato = Revision.objects.filter(nombre=nombre).last()

			datos=Add_data.objects.create(
					nombre=nombre,
					local=local,
					clima=clima,
					t_ext=exterior,
					t_int=interior,
					humedad=humedad,
					peso=peso,
					comida=comida,
					piquera=piquera,
					id_revision=dato,
					)
			direc=str(pathlib.Path().absolute())+"/beeproject2021/restbee_app/keys.json"
		 
			scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
			creds = ServiceAccountCredentials.from_json_keyfile_name(direc, scope)
			client = gspread.authorize(creds)
			sheet = client.open("Wayllapampa").sheet1   
			data = sheet.get_all_records()
			if datos.id_revision_id== None:
				revision="-"
			else:
				revision= datos.id_revision_id
				revision=Revision.objects.get(id=revision).fecha.strftime("%d/%m/%Y %H:%M:%S")
		 
			if comida ==0:
			    comida="No hay alimentador"
			else:
			    comida=datos.comida
			insertRow = [
			datos.fecha.strftime("%d/%m/%Y"),
			datos.fecha.strftime("%H:%M:%S"),
			datos.nombre,
			datos.clima,
			datos.peso,
			comida,
			datos.humedad,
			datos.t_int,
			datos.t_ext,
			datos.piquera,
			revision
			]
			sheet.append_row(insertRow)
			response={
			"value": "Correcto"
			}
			return Response(response)


		except :
			response={
			"value": "Error"
			}
			return Response(response)


class agregar_no_revisado(generics.CreateAPIView):  # READY

	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]
	def post(self, request, *args, **kwargs):
		try:
			nombre=request.data.get("nombre")
			interior = float(request.data.get("t_int"))
			interior=round(interior,2)
			# nombre=request.data.get("nombre")
			datos=No_revisado.objects.create( nombre=nombre,t_int=interior)
			direc=str(pathlib.Path().absolute())+"/beeproject2021/restbee_app/keys.json"
			# print(direc)
			scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
			creds = ServiceAccountCredentials.from_json_keyfile_name(direc, scope)
			client = gspread.authorize(creds)
			sheet = client.open("Wayllapampa").worksheet('no_supervisados') # Open the spreadhseet
			# print(sheet)
			data = sheet.get_all_records()

			insertRow = [
			datos.fecha.strftime("%d/%m/%Y"),
			datos.fecha.strftime("%H:%M:%S"),
			datos.nombre,
			datos.t_int,


			]
			sheet.append_row(insertRow)
			response={
			"value": "Correcto"
			}
			return Response(response)
		except :
			response={
			"value": "Error"
			}
			return Response(response)

class agregar_error(APIView):  # READY

	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]
	def post(self, request, *args, **kwargs):
		try:
			error=request.data.get("error")
			# nombre=request.data.get("nombre")
			datos=Errors.objects.create( error=error)
			direc=str(pathlib.Path().absolute())+"/beeproject2021/restbee_app/keys.json"
			# print(direc)
			scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
			creds = ServiceAccountCredentials.from_json_keyfile_name(direc, scope)
			client = gspread.authorize(creds)
			sheet = client.open("Wayllapampa").worksheet('error') # Open the spreadhseet
			# print(sheet)
			data = sheet.get_all_records()

			insertRow = [
			datos.fecha.strftime("%d/%m/%Y"),
			datos.fecha.strftime("%H:%M:%S"),
			datos.error


			]
			sheet.append_row(insertRow)
			response={
			"value": "Correcto"
			}
			return Response(response)
		except :
			response={
			"value": "Error"
			}
			return Response(response)

class agregar_revision(generics.CreateAPIView):  # READY

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Revision.objects.all()
    serializer_class = Revision_Serializer

 
class test(APIView):  # READY

	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]
	def post(self, request, *args, **kwargs):
		try:
			test=request.data.get("test")

			direc=str(pathlib.Path().absolute())+"/beeproject2021/restbee_app/keys.json"
			 
			scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
			creds = ServiceAccountCredentials.from_json_keyfile_name(direc, scope)
			client = gspread.authorize(creds)
			sheet = client.open("Wayllapampa").worksheet('test') # Open the spreadhseet
			# print(sheet)
			data = sheet.get_all_records()

			insertRow = [
			test


			]
			sheet.append_row(insertRow)
			response={
			"value": "Correcto"
			}
			return Response(response)
		except :
			response={
			"value": "Error"
			}
			return Response(response)
