from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('waysmart/', include('app_empresa_convenios.urls')),
    path('', RedirectView.as_view(url='/waysmart/', permanent=False)),
]