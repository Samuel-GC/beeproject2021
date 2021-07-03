from rest_framework import serializers
from restbee_app.models import *


# ###################################################################
# # ------------------Serialaizer add ------------------------------
# ###################################################################

class Add_data_Serializer(serializers.ModelSerializer):

	class Meta:
		model = Add_data
		fields = (
			"nombre",
			"ubicacion",
			"clima" ,
			"temp_Ext",
			"temp_int",
			"humedad_int",
			"peso_colmena",
			"poblacion",
			"comida" ,
			"piquera",
			"reina",
			"revision",
		)


class No_revisado_Serializer(serializers.ModelSerializer):

	class Meta:
		model = No_revisado
		fields = (
			"nombre",
			"ubicacion",
			"temp_int",
		)
