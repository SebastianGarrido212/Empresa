from django.contrib import admin
from .models import FechaBloqueada
from django.utils.html import format_html

@admin.register(FechaBloqueada)
class FechaBloqueadaAdmin(admin.ModelAdmin):
    # Columnas que se ven en la lista
    list_display = ('fecha', 'motivo_color', 'descripcion')
    
    # Filtros laterales para buscar rápido
    list_filter = ('motivo', 'fecha')
    
    # Barra de búsqueda
    search_fields = ('fecha', 'descripcion')
    
    # Navegación por fecha arriba de la lista
    date_hierarchy = 'fecha'

    # Un toque pro: Colorear el motivo en la lista
    from django.utils.html import format_html
    def motivo_color(self, obj):
        colores = {
            'FERIADO': 'red',
            'LLENO': 'orange',
            'MANTENCION': 'blue',
            'OTRO': 'gray',
        }
        color = colores.get(obj.motivo, 'black')
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            obj.get_motivo_display()
        )
    motivo_color.short_description = "Estado"
    class Media:
        css = {
            'all': (
                # Estilo Base
                'https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css',
                # TEMA VISUAL (Este arregla el fondo y las flechas) 👇
                'https://cdn.jsdelivr.net/npm/flatpickr/dist/themes/airbnb.css',
            )
        }
        js = (
            'https://cdn.jsdelivr.net/npm/flatpickr',
            'https://npmcdn.com/flatpickr/dist/l10n/es.js',
            'js/admin_calendar.js',
        )