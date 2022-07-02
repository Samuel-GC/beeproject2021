from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import generics
from restbee_app.models import *
from django.db import models
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
 
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
 
from datetime import timedelta
from django.utils.timezone import now
from django.utils import timezone
 
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
 

class LoginWeb(APIView): 

	# authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [permissions.AllowAny]
	# authentication_classes = [authentication.TokenAuthentication]
	# permission_classes = [permissions.IsAuthenticated]
	# authentication_classes = [SessionAuthentication, BasicAuthentication]
	# permission_classes = [IsAuthenticated]
	def post(self, request, *args, **kwargs):

		try:
			usuario=request.data.get("usuario")
			password=request.data.get("password")
			datos=User.objects.filter(username=usuario).last()

			if password=="":
				response={
				"value":"error",
				"mensaje":"password vacia"
				}
				return Response(response,status=status.HTTP_400_BAD_REQUEST)

			elif datos==None:
				response={
				"value":"error",
				"mensaje":"usuario no existe"
				}
				return Response(response,status=status.HTTP_400_BAD_REQUEST)
			
			elif check_password(password, datos.password):

				my_token=Token.objects.get(user_id=datos.id)
				response={
				"value":"correcto",
				"token":my_token.key,
				"nombre":usuario.capitalize(),

				}
	 
				return Response(response,status=status.HTTP_200_OK)

			else:
				response={
					"value":"error",
					"mensaje":"password incorrecta"
					}

				return Response(response,status=status.HTTP_400_BAD_REQUEST)

		except:
			response={
				"value":"error",
				"mensaje":"fallo"
				}

		return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Data_index(APIView):

	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request, *args, **kwargs):
		try:
			datos=Add_data.objects.filter(nombre="colmena_1").last()
		 
			ultima_revision=datos.id_revision.fecha
			ultima_revision=ultima_revision.strftime("%d/%m/%Y - %H:%M:%S")
			error1 = Errors.objects.filter(fecha__range=[now()-timedelta(days=1), now()])
			error=len(error1)
			response={
					"value":"correcto",
					"fecha":datos.fecha.strftime("%d/%m/%Y - %H:%M:%S"),
					"nombre":datos.nombre,
					"local":datos.local,
					"clima":datos.clima,
					"t_ext":datos.t_ext,
					"t_int":datos.t_int,
					"humedad":datos.humedad,
					"peso":datos.peso,
					"comida":datos.comida,
					"piquera":datos.piquera,
					"revision":ultima_revision,
					"error":error,

					}
			return Response(response,status=status.HTTP_200_OK)
		except:
			response={
				"value":"error",
				"mensaje":"fallo"
				}

			return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Colmena_list(APIView): 

	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request, *args, **kwargs):
		try:
			lista=[]
			nombres=Add_data.objects.all().values('nombre').distinct()

			for i in range(len(nombres)):
				
				response={
					"name": nombres[i]["nombre"],
					"value":nombres[i]["nombre"],
					}
				lista.append(response)
			return Response(lista,status=status.HTTP_200_OK)

		except:

			response={
			"value": "Error",
			}
			return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class Datos_colmena(APIView):

	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request, *args, **kwargs):
		colmena=request.data.get("nombre")
		datos=Add_data.objects.filter(nombre=colmena).last()
	 
		ultima_revision=datos.id_revision.fecha
 
		if datos.comida==0:
			comida="No hay alimentador"
		else:
			comida=str(datos.comida)+ " %"
		response={
				"value":"correcto",
				"fecha":datos.fecha.strftime("%d/%m/%Y - %H:%M:%S"),
				"nombre":datos.nombre,
				"local":datos.local,
				"clima":datos.clima,
				"t_ext":datos.t_ext,
				"t_int":datos.t_int,
				"humedad":datos.humedad,
				"peso":datos.peso,
				"comida":comida,
				"piquera":datos.piquera,
				"revision":ultima_revision.strftime("%d/%m/%Y - %H:%M:%S"),

				}
		return Response(response,status=status.HTTP_200_OK)

class Grafico_temperatura(APIView):

	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request, *args, **kwargs):
		try:
			fechas=[]
			temperatura_int=[]
			temperatura_ext=[]
			colmena=request.data.get("nombre")
			datos=Add_data.objects.filter(nombre=colmena)
	 
			for i in range(1,13,1):
				try:
					fecha=datos[len(datos)-i].fecha.strftime("%d/%m - %H:%M")
					interior=datos[len(datos)-i].t_int
					exterior=datos[len(datos)-i].t_ext
					fechas.append(fecha)
					temperatura_int.append(interior)
					temperatura_ext.append(exterior)
		 
				except:
					fechas.append("-")
					temperatura_int.append(0)
			reverse_t_int = [num for num in reversed(temperatura_int)]
			reverse_t_ext = [num2 for num2 in reversed(temperatura_ext)]
			reverse_fechas = [fec for fec in reversed(fechas)]
	 
			response={
					"value":"correcto",
					"fechas":reverse_fechas,
					"t_int":reverse_t_int,
					"t_ext":reverse_t_ext
	 

					}
			return Response(response,status=status.HTTP_200_OK)

		except:

			response={
			"value": "Error",
			}
			return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Grafico_humedad(APIView):

	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request, *args, **kwargs):
		try:
			fechas=[]
			humedad=[]
		 
			colmena=request.data.get("nombre")
			datos=Add_data.objects.filter(nombre=colmena)
	 
			for i in range(1,13,1):
				try:
					fecha=datos[len(datos)-i].fecha.strftime("%d/%m - %H:%M")
					hum=datos[len(datos)-i].humedad
				 
					fechas.append(fecha)
					humedad.append(hum)
				  
				except:
					fechas.append("-")
					humedad.append(0)
			reverse_hum = [num for num in reversed(humedad)]
		 
			reverse_fechas = [fec for fec in reversed(fechas)]
	 
			response={
					"value":"correcto",
					"fechas":reverse_fechas,
					"humedad":reverse_hum,
			 
	 

					}
			return Response(response,status=status.HTTP_200_OK)
			
		except:

			response={
			"value": "Error",
			}
			return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Grafico_comida(APIView):

	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request, *args, **kwargs):
		try:
			fechas=[]
			comida=[]
		 
			colmena=request.data.get("nombre")
			datos=Add_data.objects.filter(nombre=colmena)
	 
			for i in range(1,13,1):
				try:
					fecha=datos[len(datos)-i].fecha.strftime("%d/%m - %H:%M")
					com=datos[len(datos)-i].comida 
					fechas.append(fecha)
					comida.append(com)
					 
		 
				except:
					fechas.append("-")
					comida.append(0)
			reverse_com = [num for num in reversed(comida)]
 
			reverse_fechas = [fec for fec in reversed(fechas)]
	 
			response={
					"value":"correcto",
					"fechas":reverse_fechas,
					"comida":reverse_com,
					}
			return Response(response,status=status.HTTP_200_OK)

		except:

			response={
			"value": "Error",
			}
			return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Grafico_peso(APIView):

	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request, *args, **kwargs):
		try:
			fechas=[]
			peso=[]
			promedio=0
			colmena=request.data.get("nombre")
			datos=Add_data.objects.filter(nombre=colmena)
			
			for i in range(0,12,1):
				try:
					promedio=0
					dia=str((now()-timedelta(days=i)).strftime("%Y-%m-%d"))
					dia2=str((now()-timedelta(days=i)).strftime("%d/%m"))
					 
					valores=datos.filter(fecha__date = dia)
				 
					for y in range(len(valores)):
						promedio=promedio+valores[y].peso
			 	
					if promedio==0:
						promedio=0
					else:
						promedio=promedio/len(valores)
					promedio=round(promedio,1)
				 
					fechas.append(dia2)
					peso.append(promedio)
					 	 
				except:
					fechas.append("-")
					peso.append(0)
			reverse_peso = [num for num in reversed(peso)]

			reverse_fechas = [fec for fec in reversed(fechas)]
	 
			response={
					"value":"correcto",
					"fechas":reverse_fechas,
					"peso":reverse_peso,
					}
			return Response(response,status=status.HTTP_200_OK)

		except:

			response={
			"value": "Error",
			}
			return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Error_data(APIView):

	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request, *args, **kwargs):
		try:
			lista=[]
			hoy=now().date()
			print(hoy)
			datos=Errors.objects.filter(fecha__range=[hoy-timedelta(days=7),hoy+timedelta(days=1)])
			print(datos)
			for i in range ( len (datos)):

				response={
						"value":"correcto",
						"fecha":datos[i].fecha.strftime("%d/%m/%Y - %H:%M:%S"),
						"nombre":"colmena_1",
						"problema":datos[i].error,

						}
				lista.append(response)
			return Response(lista,status=status.HTTP_200_OK)
		except:
			response={
				"value":"error",
				"mensaje":"fallo"
				}

			return Response(response,status=status.HTTP_500_INTERNAL_SERVER_ERROR)