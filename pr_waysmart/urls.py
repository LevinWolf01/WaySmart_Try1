from django.contrib import admin
from django.urls import path, include
from pr_waysmart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('waysmart/', views.fn_inicio),
    # Las rutas del app quedan disponibles bajo /waysmart/.
    path('waysmart/', include('app_destinos_servicios.urls')),
]
