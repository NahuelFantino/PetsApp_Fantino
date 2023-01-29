from django.db import models

# Create your models here.
class Servicio(models.Model):
    id = models.AutoField(primary_key = True)
    servicio = models.CharField(max_length= 100)
    precio = models.IntegerField()
    ciudad = models.CharField(max_length= 30)
    def __str__(self):
        return f"-ID: {self.id} - Servicio: {self.servicio} - Precio de Servicio: {self.precio} - Ciudad: {self.ciudad}"

class Mascota(models.Model):
    id = models.AutoField(primary_key = True)
    especie = models.CharField(max_length= 30)
    nombre = models.CharField(max_length= 30)
    datos = models.CharField(max_length= 100)
    def __str__(self):
        return f"-ID: {self.id} - Especie: {self.especie} - Nombre: {self.nombre} - Datos adicionales: {self.datos}"

class Persona(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length= 30)
    apellido = models.CharField(max_length= 30)
    direccion = models.CharField(max_length= 100)
    def __str__(self):
        return f"-ID: {self.id} - Nombre: {self.nombre} - Apellido: {self.apellido} - Dirección: {self.direccion}"