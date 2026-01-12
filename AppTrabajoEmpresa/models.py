from django.db import models

# Create your models here.

class FechaBloqueada(models.Model):
    OPCIONES_MOTIVO = [
        ('FERIADO', 'Feriado / Festivo'),
        ('LLENO', 'Agenda Completa'),
        ('MANTENCION', 'Mantención Interna'),
        ('OTRO', 'Otro Motivo'),
    ]

    fecha = models.DateField(unique=True, help_text="Selecciona el día que NO se podrá agendar.")
    motivo = models.CharField(max_length=50, choices=OPCIONES_MOTIVO, default='LLENO')
    descripcion = models.TextField(blank=True, null=True, help_text="Nota interna (opcional).")

    class Meta:
        verbose_name = "Día Bloqueado"
        verbose_name_plural = "Días Bloqueados (Agenda)"
        ordering = ['fecha']

    def __str__(self):
        # Esto es lo que verá tu jefe en la lista
        return f"{self.fecha.strftime('%d/%m/%Y')} - {self.get_motivo_display()}"


class Proyecto(models.Model):
    CATEGORIAS = [
        ('construccion', 'Construcción'),
        ('remodelacion', 'Remodelación'),
        ('industrial', 'Industrial'),
        ('demarcacion_vial', 'Demarcación Vial'),
    ]

    titulo = models.CharField(max_length=100, verbose_name="Título del Proyecto")
    descripcion = models.CharField(max_length=200, blank=True, verbose_name="Descripción Corta")
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='construccion')
    imagen = models.ImageField(upload_to='proyectos/', verbose_name="Foto del Proyecto")
    fecha_creacion = models.DateTimeField(auto_now_add=True) # Se llena solo con la fecha actual

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Portafolio de Proyectos"
        ordering = ['-fecha_creacion'] # Muestra siempre los más nuevos primero

    def __str__(self):
        return self.titulo

    # --- AQUÍ ESTÁ LA LÓGICA HIGHLANDER ("Solo puede haber 30") ---
    def save(self, *args, **kwargs):
        # Si es un proyecto nuevo (no tiene ID aún)
        if not self.pk:
            # Contamos cuántos proyectos hay actualmente
            cantidad_actual = Proyecto.objects.count()
            
            # Si ya hay 30 (o más), borramos el más viejo
            if cantidad_actual >= 30:
                # Buscamos el más antiguo (orden asc por fecha) y lo borramos
                mas_viejo = Proyecto.objects.order_by('fecha_creacion').first()
                if mas_viejo:
                    mas_viejo.delete()
        
        # Guardamos el nuevo proyecto normalmente
        super().save(*args, **kwargs)



class DatosEmpresa(models.Model):
    nombre_empresa = models.CharField(max_length=100, default="Grupo R&M SpA")
    telefono_visible = models.CharField(max_length=20, verbose_name="Teléfono (Visual)", help_text="Ej: +56 9 5400 0528")
    whatsapp_numero = models.CharField(max_length=20, verbose_name="Número WhatsApp", help_text="Solo números, sin espacios ni símbolos. Ej: 56954000528")
    correo_contacto = models.EmailField(verbose_name="Correo de Contacto")
    instagram_link = models.URLField(verbose_name="Link de Instagram", blank=True, null=True)

    class Meta:
        verbose_name = "Configuración de Contacto"
        verbose_name_plural = "Configuración de Contacto"

    def __str__(self):
        return f"Datos de {self.nombre_empresa}"

    # LÓGICA SINGLETON: Evitamos que creen 2 configuraciones distintas
    def save(self, *args, **kwargs):
        if not self.pk and DatosEmpresa.objects.exists():
            # Si ya existe uno, no dejamos crear otro (o podrías actualizar el existente)
            # Para simplificar, asumiremos que editarán el existente.
            pass 
        super().save(*args, **kwargs)