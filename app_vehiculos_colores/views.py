from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ColorForm, VehiculoForm
from .models import Color, Vehiculo


def colores(request):
    if request.method == "POST":
        form = ColorForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "El registro de colores fue guardado correctamente."
            )

            return redirect(
                "app_vehiculos_colores:colores"
            )
    else:
        form = ColorForm()

    colores_guardados = Color.objects.all()

    return render(
        request,
        "app_vehiculos_colores/colores.html",
        {
            "form": form,
            "colores": colores_guardados,
            "titulo": "Gestión de colores",
        },
    )


def vehiculos(request):
    if request.method == "POST":
        form = VehiculoForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "El vehículo fue guardado correctamente."
            )

            return redirect(
                "app_vehiculos_colores:vehiculos"
            )
    else:
        form = VehiculoForm()

    vehiculos_guardados = Vehiculo.objects.select_related(
        "modelo",
        "color",
        "repartidor",
    )

    return render(
        request,
        "app_vehiculos_colores/vehiculo.html",
        {
            "form": form,
            "vehiculos": vehiculos_guardados,
            "titulo": "Gestión de vehículos",
        },
    )
