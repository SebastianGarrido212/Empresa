from django.contrib import admin
from .models import FechaBloqueada
from django.utils.html import format_html
from .models import Proyecto, DatosEmpresa

@admin.register(FechaBloqueada)
class FechaBloqueadaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'motivo_color', 'descripcion')
    list_filter = ('motivo', 'fecha')
    search_fields = ('fecha', 'descripcion')
    date_hierarchy = 'fecha'

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

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha_creacion')
    list_filter = ('categoria',)


@admin.register(DatosEmpresa)
class DatosEmpresaAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not DatosEmpresa.objects.exists()