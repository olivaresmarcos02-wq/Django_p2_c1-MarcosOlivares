from django.shortcuts import render
from .services import cargar_json, cargar_inicio

# Create your views here.
from django.http import HttpResponse





    

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




def catalogo(request):
    zonas = cargar_json("zonas.json")
    dispositivos = cargar_json("dispositivos.json")

    zonas_procesadas = []
    
    for zona in zonas:
        dispositivos_zona = [d for d in dispositivos if d["zona_id"] == zona["id"]]
        zona["cantidad_dispositivos"] = len(dispositivos_zona)
        zonas_procesadas.append(zona)

    context = {
        "zonas": zonas_procesadas,
    }
    return render(request, "dispositivos/catalogo.html", context)


def detalle_zona_view(request, zona_id):
    zonas = cargar_json("zonas.json")
    categorias = cargar_json("categorias.json")
    dispositivos = cargar_json("dispositivos.json")

    zona_encontrada = None
    for zona in zonas:
        if zona["id"] == int(zona_id):
            zona_encontrada = zona
            break
            
    if not zona_encontrada:
        return render(request, "404.html", status=404)

    dispositivos_zona = []
    for d in dispositivos:
        if d["zona_id"] == int(zona_id):
            for c in categorias:
                if c["id"] == d["categoria_id"]:
                    d["categoria"] = c
                    break
            dispositivos_zona.append(d)

    consumo_total = sum(d["consumo_kwh"] for d in dispositivos_zona)
    
    if consumo_total > zona_encontrada["limite_kwh"]:
        estado = "ALERTA"
        clase_badge = "bg-danger"
    else:
        estado = "NORMAL"
        clase_badge = "bg-success"

    zona_encontrada["consumo_total"] = consumo_total
    zona_encontrada["estado"] = estado
    zona_encontrada["clase_badge"] = clase_badge

    if len(dispositivos_zona) == 0:
        mensaje = "Esta zona no tiene dispositivos"
    else:
        mensaje = None

    context = {
        "zona": zona_encontrada,
        "dispositivos": dispositivos_zona,
        "sin_dispositivos_mensaje": mensaje
    }
    return render(request, "dispositivos/detalle_zona.html", context)



