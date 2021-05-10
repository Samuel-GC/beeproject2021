from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import generics
from restbee_app.models import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import *
from django.shortcuts import redirect # libreria para redireccionar paginas
from django.shortcuts import render #libreria para activar las paginas
from django.template import Template, Context #libreria para mostrar los template y enviar contextos a los html


# ------------------------- Add Datos---------------------

class agregar_data(generics.CreateAPIView):  # READY

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = add_data.objects.all()
    serializer_class = add_data_Serializer

#-----------------------vistas web ------------------------

def Index(request): 
	if request.method == "POST":
		username = request.POST['user']
		password = request.POST['password']
		print(username)
		print(password)


	return render(request,"Index.html")