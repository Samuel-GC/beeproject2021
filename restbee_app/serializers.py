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
			"local",
			"clima" ,
			"t_Ext",
			"t_int",
			"humedad",
			"peso",
			# "poblacion",
			"comida" ,
			"piquera",
			# "reina",
			"revision",
		)

class No_revisado_Serializer(serializers.ModelSerializer):

	class Meta:
		model = No_revisado
		fields = (
			"nombre",
			"local",
			"t_int",
		)

class Errors_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Errors
		fields = (
			"error",
	
		)
