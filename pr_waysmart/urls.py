from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('waysmart/', views.fn_inicio),
    path('waysmart/modelo/', include('app_modelo.urls')),
    path('waysmart/repartidor/', include('app_repartidor.urls')),
]