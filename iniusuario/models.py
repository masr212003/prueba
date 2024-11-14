from django.db import models
from django.contrib.auth.models import User



class DatosUsuario(models.Model):
    class EstadoChoices(models.TextChoices):
        ACTIVO = 'activo', 'Activo'
        INACTIVO = 'inactivo', 'Inactivo'

    nombre_usu=models.OneToOneField(User, on_delete=models.CASCADE)
    tp_usu=models.CharField(max_length=20)
    cedula=models.CharField(max_length=8)
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    telefono=models.CharField(max_length=20)
    estado=models.CharField(
        max_length=12,
        choices=EstadoChoices.choices,
        default=EstadoChoices.ACTIVO
    )


    