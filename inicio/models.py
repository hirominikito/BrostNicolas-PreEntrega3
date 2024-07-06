from django.db import models
from datetime import timezone


class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha = models.DateField(timezone)
    edad = models.IntegerField() 
    
    def __str__(self):
        return f"Alumno {self.nombre} {self.apellido}"


