from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('waysmart/', include('app_rutas_asignaciones.urls')),  # <-- Prefijo principal agregado
]