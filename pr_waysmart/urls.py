from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from pr_waysmart import views

urlpatterns = [
    path('', views.fn_inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('waysmart/', views.fn_inicio),
    path('', RedirectView.as_view(url='/waysmart/', permanent=False)),
    path('waysmart/', include('app_usuario_documento.urls')),

    # Las rutas del app quedan disponibles bajo /waysmart/.
    path('waysmart/', include('app_destinos_servicios.urls')),
    path('waysmart/', include('app_empresa_convenios.urls')), 
    path('waysmart/', include('app_PagosEntrega_TipoPago.urls')),
    path('waysmart/', include('app_rutas_asignaciones.urls')),
    path('waysmart/modelo/', include('app_modelo.urls')),
    path('waysmart/repartidor/', include('app_repartidor.urls')),
]