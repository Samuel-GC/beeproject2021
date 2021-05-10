
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.urls import path
from restbee_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

###################################################################
#------------------------add data ---------------------------------
###################################################################

    path('add/data/',agregar_data.as_view()),

###################################################################
#------------------------ Web view---------------------------------
###################################################################
path('', Index),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
