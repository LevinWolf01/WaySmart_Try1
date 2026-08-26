from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from pr_waysmart import views as views_principales

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Redirige automáticamente la raíz (/) hacia 'inicio' (/waysmart/)
    path('', lambda request: redirect('inicio', permanent=False)),
    
    # 2. La página de bienvenida asignada con el nombre 'inicio' en /waysmart/
    path('waysmart/', views_principales.fn_inicio, name='inicio'),
    
    # 3. Las rutas del módulo de pagos bajo /waysmart/pagos/
    path('waysmart/', include('app_PagosEntrega_TipoPago.urls')),
]