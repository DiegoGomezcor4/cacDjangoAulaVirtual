from django.contrib import admin
from core.models import Estudiante, Docente, Cursos, Categoria, Inscripcion

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Docente)
admin.site.register(Cursos)
admin.site.register(Categoria)
admin.site.register(Inscripcion)


