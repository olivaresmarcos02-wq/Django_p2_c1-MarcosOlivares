from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def inicio(request):
    return HttpResponse(
    "<h1>EcoEnergy</h1>"
    "<p>Back End en funcionamiento</p>"
    )

def dispositivos_zona(request, zona_id):
    tipo = {
        "nombre": "por nombre",
        "fecha": "por fecha",
        "numero": "por numero"
    }
    return render(
        request,
        "dispositivos/busqueda.html",
        tipo
    )

def busqueda(request):
    tipo = {
        "nombre": "por nombre",
        "fecha": "por fecha",
        "numero": "por numero"
    }
    return render(
        request,
        "dispositivos/busqueda.html",
        tipo
    )
    

def inicio(request):
    contexto = {
        "sistema": "EcoEnergy",
        "mensaje": "Monitoreo energético responsable",
        "asignatura": "Programación Back End",
    }
    return render(
        request,
        "dispositivos/inicio.html",
        contexto,
    )

def catalogo(request):
    dispositivos = [
        {"nombre": "Medidor inteligente", "estado": "Activo"},
        {"nombre": "Sensor de temperatura", "estado": "Activo"},
        {"nombre": "Climatizador", "estado": "Revisión"},
    ]
    return render(
        request,
        "dispositivos/catalogo.html",
        {"dispositivos": dispositivos},
    )

