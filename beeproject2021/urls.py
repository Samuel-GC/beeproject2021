
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.urls import path
from restbee_app.views import *
from web_app.views import *
from rest_web.views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),

###################################################################
#------------------------ REST - Service--------------------------- 
###################################################################

    path('add_data/cs/',agregar_data.as_view()),
    path('add_data/revision/',agregar_revision.as_view()),
    path('add_error/',agregar_error.as_view()),

###################################################################
#------------------------ Web view---------------------------------
###################################################################

	path('', Login), #redireccion al login principal
	path('inicio/', Inicio), #pagina principal
	path('colmena_datos/', Datos), #pagina de instrucciones
	path('instrucciones/', Intrucciones), #pagina de descarga
	path('nosotros/', NosotrosLogin),# Nosotros Login
	path('nosotros_in/', Nosotros),# Nosostros dentro de la app
	path('error/', Error), # Vista de error
###################################################################
#------------------------Rest - web -------------------------------
################################################################### 
	path('login_web/',LoginWeb.as_view()),
	path('index_data/',Data_index.as_view()),
	path('list/',Colmena_list.as_view()),
	path('datos/',Datos_colmena.as_view()),
	path('temperatura/',Grafico_temperatura.as_view()),
	path('humedad/',Grafico_humedad.as_view()),
	path('comida/',Grafico_comida.as_view()),
	path('peso/',Grafico_peso.as_view()),
	path('error_list/',Error_data.as_view()),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
