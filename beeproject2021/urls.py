
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.urls import path
from restbee_app.views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),

###################################################################
#------------------------add data ---------------------------------
###################################################################

    path('add_data/cs/',agregar_data.as_view()),
    path('add_data/cns/',agregar_no_revisado.as_view()),
    path('add_data/revision/',agregar_revision.as_view()),
    path('add_error/',agregar_error.as_view()),
########################-Rest - JS-########################
	# path("web/descargar/",descargar_rest.as_view()),
###################################################################
#------------------------ Web view---------------------------------
###################################################################
	path('', Login), #redireccion al login principal
	path('bee_project/', bee), #pagina principal
	path('instructions/', instrucciones), #pagina de instrucciones
	# path('descargar/', descargar), #pagina de descarga
	path('about_us/', about),# about con login
	path('historial/error/', error),# Historial de errores con login
	path('aboutus/', about2), # about sin login
###################################################################
#------------------------ Login------------------------------------
###################################################################

	path("accounts/",include("django.contrib.auth.urls")) #accounts del propio django

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
