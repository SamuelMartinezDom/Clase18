
from django.contrib import admin
from django.urls import path

from Personas.views import create_perfil
from Personas.views import lista_perfiles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empleados/', lista_perfiles),
    path('nuevo_empleado/', create_perfil)
]
