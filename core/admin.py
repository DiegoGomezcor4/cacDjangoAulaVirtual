from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ManyToManyField
from django.forms.models import ModelMultipleChoiceField
from django.http.request import HttpRequest
from core.models import Estudiante, Docente, Cursos, Categoria, Inscripcion

"""
class CacAdminSite(admin.AdminSite): # modificando el admin site
    site_header = 'Sistema de administracion del Aula Virtual 2.0'
    site_title = 'Administracion para superusers'
    index_title = 'Administracion del Sitio'
    empty_value_display = 'vacio'
"""

class EstudianteAdmin(admin.ModelAdmin): # modifica la visualizacion en el admin
    list_display = ('legajo', 'apellido', 'nombre')
    list_editable = ('apellido', 'nombre')
    list_display_links = ['legajo']
    search_fields = ['apellido']
    


@admin.register(Cursos)
class CursoAdmin(admin.ModelAdmin):
    list_display= ('nombre', 'fecha_inicio')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'estudiantes':
            kwargs['queryset'] = Estudiante.objects.filter().order_by('apellido')

        return super().formfield_for_manytomany(db_field, request, **kwargs)



# Register your models here.
"""
sitio_admin = CacAdminSite(name='cacadmin')
sitio_admin.register(Estudiante, EstudianteAdmin)
sitio_admin.register(Docente)
sitio_admin.register(Categoria)
sitio_admin.register(Inscripcion)
sitio_admin.register(Cursos)
"""

admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Docente)
admin.site.register(Categoria)
admin.site.register(Inscripcion)
#admin.site.register(Cursos)

