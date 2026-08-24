from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('modelo/', include('app_modelo.urls')),
    path('repartidor/', include('app_repartidor.urls')),
]