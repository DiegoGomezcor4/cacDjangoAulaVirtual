from django.db import models
from django.forms import ValidationError

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    apellido = models.CharField(max_length=30, verbose_name='Apellido')
    email = models.EmailField(max_length=150, verbose_name='Email')
    dni = models.IntegerField(verbose_name='dni', unique=True) # validacion por base de datos capo unico
    
    
        
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    
    
    def __str__(self):
        return self.nombre_completo()
        
    class Meta:
        abstract = True
    

class Estudiante(Persona):
    legajo = models.CharField(max_length=100, verbose_name='Legajo')
    
    
class Docente(Persona):
    cuit = models.CharField(max_length=100, verbose_name='cuit')
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')

    def __str__(self):
        return self.nombre
    
class Cursos(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    descripcion = models.CharField(max_length=150, verbose_name='Descripcion del curso')
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio')
    cantidad_clases = models.IntegerField(verbose_name='Cantidad de clases')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(Estudiante, through="Inscripcion") # esto me falta para corregir mi proyecto

    def __str__(self):
        return f"{self.nombre} {self.fecha_inicio}"


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha de inscripcion")

    def __str__(self):
        return f"{self.estudiante.nombre_completo()} - {self.curso} - {self.fecha}"