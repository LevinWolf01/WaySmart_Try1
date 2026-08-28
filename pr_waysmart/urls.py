from django.contrib import admin
from django.urls import include, path
from pr_waysmart import views



urlpatterns = [
    path("admin/", admin.site.urls),
    path('waysmart/', views.fn_inicio),
    path("waysmart/",include("app_vehiculos_colores.urls")),
]



