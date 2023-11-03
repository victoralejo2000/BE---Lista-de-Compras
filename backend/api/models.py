from django.db import models

# Create your models here.
class Tarea(models.Model):
    
    ESTADO_CHOICES = (
        ('pendiente','Pendiente'),
        ('completado','Completado')
    )
    
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=50,choices=ESTADO_CHOICES)
    
    def __str__(self):
        return self.descripcion


class Producto(models.Model):
    ESTADO_CHOICES = (
        ('vendido','vendido'),
        ('por vender','por vender')
    )
    articulo = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)
    detalle = models.TextField(max_length=200)
    estado = models.CharField(max_length=100,choices=ESTADO_CHOICES)
    total = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.articulo