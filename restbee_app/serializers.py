from rest_framework import serializers
from restbee_app.models import *


# ###################################################################
# # ------------------Serialaizer add ------------------------------
# ###################################################################

class add_data_Serializer(serializers.ModelSerializer):

	class Meta:
		model = add_data
		fields = (
			'nombre',
			"clima" ,
			"temp_Ext"
			"temp_int",
			"humedad_int",
			"peso_colmena",
			"poblacion",
			"comida" ,
			"piquera_abierta",
			"reina_dentro",
			"revision"
		)

