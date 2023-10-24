from django.db import models
from django.forms import ValidationError

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    apellido = models.CharField(max_length=30, verbose_name='Apellido')
    email = models.EmailField(max_length=150, verbose_name='Email')
    dni = models.IntegerField(verbose_name='DNI')
    
    def clean_dni(self):
        if not (0 < self.cleaneed_data['dni'] <= 99999999):
            raise ValidationError('el dni debe ser un numero positivo de 8 digitos')
        return self.cleaneed_data['dni']
        
    class Meta:
        abstract = True
    

class Estudiante(Persona):
    legajo = models.CharField(max_length=100, verbose_name='Legajo')
    
    
class Docente(Persona):
    cuit = models.CharField(max_length=100, verbose_name='cuit')
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    
class Cursos(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    descripcion = models.CharField(max_length=150, verbose_name='Descripcion del curso')
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio')
    cantidad_clases = models.IntegerField(verbose_name='Cantidad de clases')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(Estudiante)
    