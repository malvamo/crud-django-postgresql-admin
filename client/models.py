from django.db import models  # Importa el módulo de modelos de Django

class Registro(models.Model):
    
    # Modelo para guardar los registros con nombre y correo

    nombre = models.CharField(max_length=100)   # Campo de texto limitado
    correo = models.EmailField(unique=True)     # Campo de email, debe ser único
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha automática al crear

    def __str__(self):
        # Muestra un resumen del objeto al imprimirlo
        return f'{self.nombre} ({self.correo})'