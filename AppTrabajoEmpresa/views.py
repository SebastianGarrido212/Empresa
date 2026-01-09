from django.shortcuts import render
import json
from datetime import date
from .models import FechaBloqueada, Proyecto
from .utils import obtener_feriados

# Create your views here.
def index(request):
    # 1. Obtener bloqueos manuales desde la Base de Datos
    bloqueos_db = list(FechaBloqueada.objects.values_list('fecha', flat=True))
    bloqueos_db_str = [fecha.strftime("%Y-%m-%d") for fecha in bloqueos_db]
    
    # 2. Obtener feriados automáticos (Año actual y próximo)
    year_actual = date.today().year
    feriados_actual = obtener_feriados(year_actual)
    feriados_prox = obtener_feriados(year_actual + 1)
    
    # 3. Fusionar listas (Set para eliminar duplicados)
    todas_fechas = set(bloqueos_db_str + feriados_actual + feriados_prox)
    
    # 4. Convertir a lista y serializar
    lista_final = list(todas_fechas)
    fechas_json = json.dumps(lista_final)
    ultimos_proyectos = Proyecto.objects.all()[:4]

    context = {
        'fechas_ocupadas': fechas_json,
        'ultimos_proyectos': ultimos_proyectos
    }
    
    return render(request, 'index.html', context)

def nosotros(request):
    return render(request, 'about.html')


def portfolio(request):
    todos_los_proyectos = Proyecto.objects.all()
    
    context = {
        'proyectos': todos_los_proyectos
    }
    return render(request, 'portfolio.html', context)
