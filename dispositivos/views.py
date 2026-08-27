from django.shortcuts import render
from .services import cargar_dispositivos, cargar_inicio

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
    inicio = cargar_inicio
    contexto = {
        "info" : inicio,
    }
    return render(
        request,
        "dispositivos/inicio.html",
        contexto,
    )

def catalogos(request):
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

def catalogo(request):

    dispositivos = cargar_dispositivos()

    activos = sum(
        1 for item in dispositivos
        if item["estado"] == "Activo"
    )

    contexto = {
        "dispositivos": dispositivos,
        "total": len(dispositivos),
        "total_activos": activos,
    }

    return render(
        request, "dispositivos/catalogo.html", contexto
    )


