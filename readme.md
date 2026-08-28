## WaySmart

Proyecto Django del equipo.

### Ejecutar localmente

Desde la carpeta que contiene `manage.py`:

```powershell
python manage.py migrate
python manage.py runserver
```

### Rutas del modulo usuario-documento

- Usuarios: `http://127.0.0.1:8000/waysmart/usuario/`
- Documentos: `http://127.0.0.1:8000/waysmart/documento/`

El entorno virtual, la base de datos SQLite local y las cachés de Python están excluidos mediante `.gitignore`.