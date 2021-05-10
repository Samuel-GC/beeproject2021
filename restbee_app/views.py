from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import generics
from restbee_app.models import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import *


# ------------------------- Add Datos---------------------

class agregar_data(generics.CreateAPIView):  # READY

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = add_data.objects.all()
    serializer_class = add_data_Serializer

