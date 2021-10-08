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

###########################################################
#-----------------------Rest APP---------------------------
###########################################################

# class agregar_data(generics.CreateAPIView):  # READY

#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Add_data.objects.all()
#     serializer_class = Add_data_Serializer

class agregar_data(generics.CreateAPIView):  # READY

	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]
	def post(self, request, *args, **kwargs):
		try:
			nombre = request.data.get("nombre")
			local = request.data.get("local")
			clima = request.data.get("clima")
			exterior = request.data.get("t_ext")
			interior = request.data.get("t_int")
			humedad = request.data.get("humedad")
			peso = request.data.get("peso")
			comida = request.data.get("comida")
			piquera = request.data.get("piquera")
			# print(nombre)
			dato = Revision.objects.filter(nombre=nombre).last()
			# print(dato)
			# if len(dato)==0:
			# 	dato=None
			# else:
			# 	dato=dato[0].id
			# print("aqui")
			Add_data.objects.create(
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
    queryset = No_revisado.objects.all()
    serializer_class = No_revisado_Serializer

class agregar_error(generics.CreateAPIView):  # READY

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Errors.objects.all()
    serializer_class = Errors_Serializer


class agregar_revision(generics.CreateAPIView):  # READY

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Revision.objects.all()
    serializer_class = Revision_Serializer

class descargar_rest(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            lista=[]
            lista.append(["ID",
                "Fecha",
                "Nombre",
                "Ubicacion",
                "Clima",
                "Temperatura Externa",
                "Temperatura Interna",
                "Humedad",
                "Peso",
                # "Poblacion",
                "Comida",
                "Piquera",
                # "Reina",
                # "Revision",
                ])
            fecha1 = request.data.get("fecha1")
            fecha2 = request.data.get("fecha2")
            dato=Add_data.objects.filter(fecha__range=[fecha1, fecha2])
            for i in range(len(dato)):
         
                diccionario =[dato[i].id,
					dato[i].fecha.strftime("%Y-%m-%d %H:%M:%S") ,
					dato[i].nombre,
					dato[i].local,
					dato[i].clima,
					dato[i].t_ext,
					dato[i].t_int,
					dato[i].humedad,
					dato[i].peso_colmena,
					# dato[i].poblacion,
					dato[i].comida,
					dato[i].piquera,
					# dato[i].reina,
					# dato[i].revision.strftime("%Y-%m-%d %H:%M:%S"),
					]  
    
                lista.append(diccionario)

            return Response(lista)
        except:
            dato = None
            diccionario = {
                "value": "Error",
            }
            return Response(diccionario)

###########################################################
#-----------------------vistas web ------------------------
###########################################################
def Login(request):
	return redirect('/accounts/login/')


@login_required
def bee(request):
	try:
		if request.method == "GET":
			current_user = request.user.username

			col1 = Add_data.objects.filter(nombre="colmena_1").last()
			col2 = Add_data.objects.filter(nombre="colmena_2").last()
			# col3 = Add_data.objects.filter(nombre="colmena_3").last()
			col1_r = Revision.objects.filter(nombre="colmena_1").last()
			col2_r = Revision.objects.filter(nombre="colmena_2").last()
			# col3_ = Add_data.objects.filter(nombre="colmena_3").last()
			col_ns_1 = No_revisado.objects.filter(nombre="colmena_ns_1").last()
			col_ns_2 = No_revisado.objects.filter(nombre="colmena_ns_2").last()
			# print(now())
			error1 = Errors.objects.filter(fecha__range=[now()-timedelta(days=1), now()])
			error=len(error1)
			# print(error)
			# urgente=pedidos_generados.filter(prioridad_pedido="Urgente")
			# regular=pedidos_generados.filter(prioridad_pedido="Regular")
			diccionario = {
			"usuario":current_user.capitalize(),
			"col_s_1":col1,
			"col_s_2":col2 ,
			"revision_1":col1_r,
			"revision_2":col2_r ,
			# "col_s_3":col3 ,
			"col_n_1":col_ns_1 ,
			"col_n_2":col_ns_2,
			"error":error,
			}
			return render(request,"bee.html",diccionario)

		else:
			return render(request,"bee.html")
	except:
		return redirect('/accounts/login/')

@login_required
def instrucciones(request):
	return render(request,"instrucciones.html")


	
@login_required
def about(request):
	return render(request,"aboutus.html")

	

@login_required
def descargar(request):
	return render(request,"descargar.html")

@login_required
def error(request):
	try:
		if request.method == "GET":
			error1=Errors.objects.filter(fecha__range=[now()-timedelta(days=30), now()])
			# print(error)
			error=error1.order_by('-fecha')
			diccionario = {
			
			"error":error,

			}
			return render(request,"error.html",diccionario)

		else:
			return render(request,"bee.html")
	except:
		return redirect('/accounts/login/')	
	# return render(request,"error.html")
	

def about2(request):
	return render(request,"aboutus2.html")