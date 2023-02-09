"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project1.views import saludo,lista,fecha,calculaEdad,cambiante_uno,cambiante_dos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('lista/', lista),
    path('fecha/', fecha),
    #Agrego a la url que lleva un parametro
    #Para pasar 2 parametros en la ruta es asi: edades/18/2222
    path('edades/<int:edad>/<int:agno>', calculaEdad), # el int:agno lo convierte a entero
    path('cambiante_uno/', cambiante_uno),
    path('cambiante_dos/', cambiante_dos),
]
