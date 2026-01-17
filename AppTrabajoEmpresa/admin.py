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


from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_formato', 'imagen_preview', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('fecha_creacion',)
    readonly_fields = ('imagen_preview',)

    def precio_formato(self, obj):
        if obj.precio:
            return f"${obj.precio:,}".replace(",", ".")
        return "Consultar"
    precio_formato.short_description = "Precio"

    def imagen_preview(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 5px;" />', obj.imagen.url)
        return "Sin imagen"
    imagen_preview.short_description = "Vista Previa"

from .models import Testimonio

@admin.register(Testimonio)
class TestimonioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'comentario_preview', 'aprobado', 'fecha_creacion')
    list_filter = ('aprobado', 'fecha_creacion')
    list_editable = ('aprobado',)
    search_fields = ('nombre', 'comentario')

    def comentario_preview(self, obj):
        return obj.comentario[:50] + "..." if len(obj.comentario) > 50 else obj.comentario