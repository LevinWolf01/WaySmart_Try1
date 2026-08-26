from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.shortcuts import redirect
from pr_waysmart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('waysmart/', views.fn_inicio),
    path('', RedirectView.as_view(url='/waysmart/', permanent=False)),
  
    # Las rutas del app quedan disponibles bajo /waysmart/.
    path('waysmart/', include('app_destinos_servicios.urls')),
    path('waysmart/', include('app_empresa_convenios.urls')), 
    path('waysmart/', include('app_PagosEntrega_TipoPago.urls')),
]