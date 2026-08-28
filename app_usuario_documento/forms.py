from django import forms

from .models import Documento, Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'contraseña', 'rol', 'estado']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }


class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
            'tipo_documento',
            'url_archivo',
            'estado',
            'usuario',
            'entidad_tipo',
            'entidad_id',
        ]
