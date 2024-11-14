from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    class EstadoChoices(models.TextChoices):
        ACTIVO = 'activo', 'Activo'
        INACTIVO = 'inactivo', 'Inactivo'

    nombre=models.CharField(max_length=20)
    estado = models.CharField(
        max_length=12,
        choices=EstadoChoices.choices,
        default=EstadoChoices.ACTIVO
    )
    
    def __str__(self):
        return self.nombre

class Marca(models.Model):
    class EstadoChoices(models.TextChoices):
        ACTIVO = 'activo', 'Activo'
        INACTIVO = 'inactivo', 'Inactivo'

    nombreMar=models.CharField(max_length=20)
    estado = models.CharField(
        max_length=12,
        choices=EstadoChoices.choices,
        default=EstadoChoices.ACTIVO
    )
    
    def __str__(self):
        return self.nombreMar

class Productos(models.Model):
    class EstadoChoices(models.TextChoices):
        ACTIVO = 'activo', 'Activo'
        INACTIVO = 'inactivo', 'Inactivo'
     

    nombre=models.CharField(max_length=30)
    peso=models.CharField(max_length=30)
    precio=models.FloatField()
    cantidad=models.IntegerField()
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca=models.ForeignKey(Marca, on_delete=models.CASCADE)
    estado = models.CharField(
        max_length=12,
        choices=EstadoChoices.choices,
        default=EstadoChoices.ACTIVO
    )

    imagen = models.ImageField(upload_to='productos/') 

    def __str__(self):
        return self.nombre

class CarritoProducto(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio=models.FloatField()
    precioFin=models.FloatField()
    user=models.CharField(max_length=20)


class Ordene(models.Model):
    class EstadoChoices(models.TextChoices):
        PENDIENTE = 'pendiente', 'Pendiente'
        EN_PROCESO = 'en_proceso', 'En Proceso'
        COMPLETADA = 'completada', 'Completada'
        CANCELADA = 'cancelada', 'Cancelada'

    productos = models.ManyToManyField(Productos)
    receptor = models.CharField(max_length=20)
    referencia = models.IntegerField()
    total=models.FloatField()
    ubicacion = models.CharField(max_length=20)
    usuario = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=12,
        choices=EstadoChoices.choices,
        default=EstadoChoices.PENDIENTE
    )

class OrdeneProducto(models.Model): 
    orden = models.ForeignKey(Ordene, on_delete=models.CASCADE) 
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE) 
    cantidad = models.IntegerField()