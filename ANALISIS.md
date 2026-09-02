# Relaciones, Multiplicidades y Claves de conexion
Relación Zona a Dispositivos (1:N)
    -Descripción: Una zona geográfica o estructural agrupa múltiples dispositivos de monitoreo       energético.  
    -Multiplicidad: 1 Zona (0..*) Dispositivos.  
    -Clave de conexión: El campo zona_id presente en cada objeto de dispositivos.json actúa como clave foránea lógica que enlaza con el campo id de zonas.json.  

Relación Categoría a Dispositivos (1:N)
    -Descripción: Una categoría clasifica a uno o varios dispositivos según su tipo o naturaleza técnica.  
    -Multiplicidad: 1 Categoría (0..*) Dispositivos.  
    -Clave de conexión: El campo categoria_id en dispositivos.json vincula con el campo id de categorias.json.  

# Criterios de Aceptacion(CA), Archivo/Componente(A/C), Prueba(P)

# 1
CA-01 a CA-02: Carga de datos y ListadoEl listado muestra todas las zonas registradas con su nombre,    límite y cantidad de dispositivos.  

A/C: dispositivos/views.py (catalogo) / catalogo.html

P: Acceder a la ruta principal o de catálogo y verificar visualmente que las tarjetas muestren dinámicamente la información de zonas.json y el conteo de dispositivos.  

# 2
CA-03 a CA-05: Detalle, Consumo y EstadosEl detalle muestra dispositivos, categoría, consumo total y calcula dinámicamente los estados NORMAL o ALERTA según el límite.

A/C: dispositivos/views.py (detalle_zona_view) / detalle_zona.html

P: Entrar al detalle de una zona (/zonas/<id>/) y comprobar el cálculo acumulado en kWh, el cambio de indicador visual y texto descriptivo. 

# 3
CA-06 y CA-07: Comportamiento Dinámico y Colección VacíaLa aplicación incorpora nuevos registros automáticamente y maneja zonas sin dispositivos de forma operativa.  

A/C: dispositivos/views.py / detalle_zona.html

P: Agregar dispositivos al JSON de prueba o dejar una zona sin ellos para verificar la estabilidad de la interfaz y la lectura del mensaje alternativo.  

# 4
CA-08: Gestión de Excepciones 404Un identificador de zona inexistente responde de forma controlada mediante una página de error 404.  

A/C: dispositivos/views.py / 404.html / config/urls.py

P: Navegar deliberadamente a una ruta no registrada (ej. /zonas/999/) y comprobar la respuesta HTTP controlada.  
# 5
CA-09 a CA-12: Usabilidad y Diseño ResponsiveLa interfaz conserva su estructura, maneja tablas adaptativas con desplazamiento y aplica jerarquía visual coherente con Bootstrap.  

A/C: Plantillas HTML (base.html, tablas y tarjetas)

P: Revisión de los componentes visuales bajo distintas volumetrías de datos asegurando que los controles y la navegación permanezcan accesibles. 

# 6
CA-13: Integridad del ProyectoEl proyecto puede instalarse, configurar dependencias, ejecutar Django y superar python manage.py check.  

A/C: manage.py / requirements.txt / Configuración general

P: Ejecución de la validación del sistema en la terminal para certificar la ausencia de errores de configuración.  