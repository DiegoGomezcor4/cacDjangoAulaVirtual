from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import ContactoForm, AltaAlumnoForm
from .models import Docente, Estudiante
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

def index(request):
    context = {
       'usuario' : "DIEGO",
       'fecha' : datetime.now(),
       'es_instructor': False
    }
    return render(request, "core/index.html", context)

def contacto(request):
        
        if request.method == 'POST':

            #instaciamos un formulario con datos
            contacto_form = ContactoForm(request.POST)

            #validarlo
            if contacto_form.is_valid():

                messages.info(request, "Consulta enviada con exito")
                
                p1 = Estudiante(
                    nombre=contacto_form.cleaned_data['nombre'],
                    apellido=contacto_form.cleaned_data['apellido'],
                    email=contacto_form.cleaned_data['mail'],
                    dni=contacto_form.cleaned_data['dni'],
                    legajo=contacto_form.cleaned_data['legajo']
                )
                p1.save()
                
                #dar de alta la informacion
                return redirect(reverse('index'))


        else: #get
            contacto_form = ContactoForm()

        return render(request, 'core/contacto.html',{'contacto_form' : contacto_form})
     
        

def alta_alumno(request):
    context = {}
    
    if request.method == 'POST':
        alta_alumno_form = AltaAlumnoForm(request.POST)
        
        if alta_alumno_form.is_valid():
            nuevo_alumno = Estudiante(
                nombre= alta_alumno_form.cleaned_data['nombre'],
                apellido= alta_alumno_form.cleaned_data['apellido'],
                email= alta_alumno_form.cleaned_data['email'],
                dni= alta_alumno_form.cleaned_data['dni'],
                legajo= alta_alumno_form.cleaned_data['legajo'],
            )
            nuevo_alumno.save()
        
            messages.info(request, "alumno dado de alta correctamente")
            return redirect(reverse('alumnos_listado'))

    # else:
    #     alta_form_form = AltaAlumnoForm()
        
    context['alta_alumno_form'] = AltaAlumnoForm()
    
    return render(request, 'core/alta_alumno.html', context)


    
def alumnos_listado(request):
   
   listado = Estudiante.objects.all().order_by('dni')
   
   # esta data vendra de la base de datos
#    listado = [
#         'carlos lopez',
#            'maria del cerro',
#            'juan perez',
#            'patricio estrella',
#            'bob sponja'
#    ]

   context = {
       'usuario' : "DIEGO",
       'fecha' : datetime.now(),
       'es_instructor': False,
       'cant_inscriptos' : 0,
       'listado_alumnos' : listado,
       'cant_inscriptos' : len(listado)
    }
   return render(request, "core/alumnos_listado.html", context)


def alumnos_detalle(request, nombre_alumno):
    return HttpResponse(
        f"""
        <h1>Bienvenido {nombre_alumno} </h1>
        <p>Pagina Personal de usuario</p>
        """
    )


def alumnos_historico(request, year):
    return HttpResponse(f"<h1> historico de alumnos del año: {year}</h1>")



def alumnos_estado(request, estado):
    return HttpResponse(f"<h1> filtrar alumnos por estado: {estado}</h1>")


def alumnos_detalle_activos(request, nombre_alumno):
    nombre_a = nombre_alumno

    context = {
        'nombre' : nombre_a
    }

    return render(request, "core/alumnos_detalle_activos.html", context)


# vistas basadas en clases

class DocenteListView(ListView):
    model = Docente
    context_object_name = 'listado_docentes'
    template_name = 'core/docentes_listado.html'
    ordering = ['cuit']

class DocenteCreateView(CreateView):
    pass