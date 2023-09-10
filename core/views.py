from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hola gente")


def alumnos_listado(request):
    return HttpResponse("""
         <ul>
                <li>pepe</li>
                <li>maria</li>
                <li>bruno</li>               
        </ul>
        """)
