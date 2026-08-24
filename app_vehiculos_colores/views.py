from django.http import HttpResponse

def inicio(request):
    return HttpResponse("¡Bienvenido a la sección de Vehículos y Colores!")
