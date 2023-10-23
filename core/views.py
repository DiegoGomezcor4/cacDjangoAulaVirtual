from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import ContactoForm
from .models import Persona

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
                
                p1 = Persona(
                    nombre=contacto_form.cleaned_data['nombre'],
                    apellido=contacto_form.cleaned_data['apellido'],
                    email=contacto_form.cleaned_data['mail'],
                    dni=contacto_form.cleaned_data['dni']
                )
                p1.save()
                
                #dar de alta la informacion
                return redirect(reverse('index'))


        else: #get
            contacto_form = ContactoForm()

        return render(request, 'core/contacto.html',{'contacto_form' : contacto_form})
        


def alumnos_listado(request):
   
   listado = Persona.objects.all()
   
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
