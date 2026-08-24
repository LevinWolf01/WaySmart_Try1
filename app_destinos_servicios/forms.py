from django import forms

from .models import Destino, Servicio


class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = '__all__'
        widgets = {
            'fecha_entrega': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'
        widgets = {
            'fecha_deseada': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }