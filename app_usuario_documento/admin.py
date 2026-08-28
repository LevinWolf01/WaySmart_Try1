from django.contrib import admin

# Register your models here.
from .models import Usuario, Documento

admin.site.register(Usuario)
admin.site.register(Documento)
