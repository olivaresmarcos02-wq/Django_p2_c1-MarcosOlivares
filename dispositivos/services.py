# dispositivos/services.py

import json

from django.conf import settings

def cargar_dispositivos():
    ruta = settings.BASE_DIR / "data" / "dispositivos.json"

    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)

    if not isinstance(datos, list):
        raise ValueError("Se esperaba una lista de dispositivos")
    return datos

def cargar_inicio():
    ruta = settings.BASE_DIR / "data" / "inicio.json"
    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if not isinstance(datos, list):
        raise ValueError("Se esperaba una lista de dispositivos")
    return datos

def cargar_json(nombre_archivo):
    ruta = settings.BASE_DIR / "data" / nombre_archivo
    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if not isinstance(datos, list):
        raise ValueError(f"{nombre_archivo} debe contener una lista")
    return datos

zonas = cargar_json("zonas.json")
categorias = cargar_json("categorias.json")
dispositivos = cargar_json("dispositivos.json")
