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