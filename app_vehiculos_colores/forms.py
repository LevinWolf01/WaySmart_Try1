from django import forms

from .models import Color, Vehiculo


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ["rojo", "amarillo", "verde", "negro"]
        widgets = {
            "rojo": forms.NumberInput(attrs={
                "min": 0,
                "class": "form-control"
            }),
            "amarillo": forms.NumberInput(attrs={
                "min": 0,
                "class": "form-control"
            }),
            "verde": forms.NumberInput(attrs={
                "min": 0,
                "class": "form-control"
            }),
            "negro": forms.NumberInput(attrs={
                "min": 0,
                "class": "form-control"
            }),
        }


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = [
            "modelo",
            "color",
            "repartidor",
            "tipo",
            "marca",
            "linea",
            "placa",
            "estado",
            "observacion_rechazo",
            "activo",
            "fecha_validacion",
        ]

        widgets = {
            "modelo": forms.Select(attrs={"class": "form-control"}),
            "color": forms.Select(attrs={"class": "form-control"}),
            "repartidor": forms.Select(attrs={"class": "form-control"}),
            "tipo": forms.Select(attrs={"class": "form-control"}),
            "marca": forms.TextInput(attrs={"class": "form-control"}),
            "linea": forms.TextInput(attrs={"class": "form-control"}),
            "placa": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "ABC123"
            }),
            "estado": forms.Select(attrs={"class": "form-control"}),
            "observacion_rechazo": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),
            "activo": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),
            "fecha_validacion": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local"
                },
                format="%Y-%m-%dT%H:%M"
            ),
        }