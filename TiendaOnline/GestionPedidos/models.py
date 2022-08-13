from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Cliente") #verbose_name is change in panel admin
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=10)
    def __str__(self):
        return 'nombre: %s\n' % (self.nombre)

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=50)
    precio = models.IntegerField()
    def __str__(self):
        return 'nombre: %s\n seccion: %s\n Precio: %s\n' % (self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
    def __str__(self):
        return 'No. Pedido: %s\n Estado: %s' % (self.numero, self.entregado)