#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Instalar librerías
pip install -r requirements.txt

# 2. Preparar archivos estáticos (CSS, imágenes)
python manage.py collectstatic --noinput

# 3. Crear las tablas en la Base de Datos (Migrate)
python manage.py migrate
