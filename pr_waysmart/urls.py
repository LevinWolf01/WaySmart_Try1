from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from .import views
from pr_waysmart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('waysmart/', views.fn_inicio),
    path('vehiculos-colores/', include('app_vehiculos_colores.urls')),
    ]


