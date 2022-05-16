from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import generics
from restbee_app.models import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# from .serializers import *
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
#-----------------------vistas web ------------------------
###########################################################
def Login(request):
	return render(request, "index.html")

def Inicio(request):
	return render(request, "index.html")

def Datos(request):
	return render(request, "index.html")

def Intrucciones(request):
	return render(request, "index.html")

def Error(request):
	return render(request, "index.html")

def NosotrosLogin(request):
	return render(request, "index.html")

def Nosotros(request):
	return render(request, "index.html")
 