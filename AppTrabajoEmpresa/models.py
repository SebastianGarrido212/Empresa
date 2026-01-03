from django.db import models

# Create your models here.
class FechaOcupada(models.Model):
    fecha = models.DateField(unique=True)
    motivo = models.CharField(max_length=100, default="Ocupado")

    def __str__(self):
        return f"{self.fecha} - {self.motivo}"