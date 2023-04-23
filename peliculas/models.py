from django.db import models

# Create your models here.

class Pelicula(models.Model):
    id=models.CharField(primary_key=True, max_length=4)
    nombre=models.CharField(max_length=60)
    duracion=models.DurationField(max_length=3)
    productora=models.CharField(max_length=100)
    fecha_estreno=models.DateField()
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.id, self.nombre)
