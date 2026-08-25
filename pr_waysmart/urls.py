from django.contrib import admin
from django.urls import path, include
from pr_waysmart import views

urlpatterns = [
    path('', views.fn_inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('app_usuario_documento/', include('app_usuario_documento.urls')),
]