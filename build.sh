#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Instalar librerías
pip install -r requirements.txt

# 2. Preparar archivos estáticos (CSS, imágenes)
python manage.py collectstatic --noinput

# 3. Crear las tablas en la Base de Datos (Migrate)
python manage.py migrate

# 4. Crear Superusuario Automático (El truco)
# Esto crea un código Python temporal que revisa si existe 'admin'. Si no, lo crea.
python -c "
import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TrabajoEmpresa.settings')
django.setup()

User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('SUPERUSUARIO CREADO: admin / admin123')
else:
    print('El superusuario ya existe.')
"