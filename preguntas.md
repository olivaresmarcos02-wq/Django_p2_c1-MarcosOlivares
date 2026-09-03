Respuestas
Pregunta1: La solicituda llega a /resumen-zonas/ que es enviada a la views, de ahí la función lógica ejecuta los archivos json que se están almacenados en services.py en cargar_datos, luego de hacer la lógica en las views se envían a los templates y porteriormente los html muestran los datos

Pregunta2: views.py muestra la función resumen_zona y ahí la variable 
    for zona in zonas:
            dispositivos_zona = [d for d in dispositivos if d["zona_id"] == zona["id"]]
            zona["cantidad_dispositivos"] = len(dispositivos_zona)
            zonas_procesadas.append(zona)
cuenta dispositivos, y la variable:
    consumo_total = sum(d["consumo_kwh"] for d in dispositivos_zona)
suma el consumo

pregunta3:
    if consumo_total > zona_encontrada["limite_kwh"]:
            estado = "ALERTA"
            clase_badge = "bg-danger"
        else:
            estado = "NORMAL"
            clase_badge = "bg-success"
si el consumo total supera la zona encontrada muestra el estado alerta, si no la supera muestra el estado total
    if len(dispositivos_zona) == 0:
            mensaje = "Esta zona no tiene dispositivos"
        else:
            mensaje = None
si al recorrer el json de dispositivos este no tiene la zona muestra que no estan
