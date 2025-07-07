# emergencias/models.py

from django.db import models
from django.utils import timezone

class AlertaEmergencia(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15, blank=True)
    ubicacion = models.CharField(max_length=255)  # Dirección generada desde lat/lng
    fecha_hora = models.DateTimeField(default=timezone.now)
    atendido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} - {self.ubicacion} - {self.fecha_hora}"
