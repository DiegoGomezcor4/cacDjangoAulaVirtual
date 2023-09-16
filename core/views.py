from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")


def alumnos_listado(request):
   context = {
       'usuario' : "DIEGO",
       'fecha' : datetime.now(),
       'es_instructor': False,
    }
   return render(request, "alumnos_listado.html", context)


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