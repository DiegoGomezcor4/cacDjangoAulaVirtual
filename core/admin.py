from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ManyToManyField
from django.forms.models import ModelMultipleChoiceField
from django.http.request import HttpRequest
from core.models import Estudiante, Docente, Cursos, Categoria, Inscripcion

class EstudianteAdmin(admin.ModelAdmin): # modifica la visualizacion en el admin
    list_display = ('legajo', 'apellido', 'nombre')
    list_editable = ('apellido', 'nombre')
    list_display_links = ['legajo']
    search_fields = ['apellido']


class CursoAdmin(admin.ModelAdmin):
    list_display= ('nombre', 'fecha_inicio')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'estudiantes':
            kwargs['queryset'] = Estudiante.objects.filter(legajo__startswith='2').order_by('apellido')

        return super().formfield_for_manytomany(db_field, request, **kwargs)

# Register your models here.
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Docente)
admin.site.register(Cursos)
admin.site.register(Categoria)
admin.site.register(Inscripcion)


