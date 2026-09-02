# Herramienta
Nombre: Gemini (Google)

# Prompts 
Generación y adaptación de plantillas (catalogo.html, detalle_zona.html, 404.html y busqueda.html) para integrarlas con la barra de navegación y la estructura provista por el usuario.

Asistencia en la resolución de errores de compilación

# Respuesta Utilizada
Estructura lógica para las funciones de vista (catalogo, detalle_zona_view) encargadas de cruzar IDs, sumarizar consumos en kWh y calcular estados de alerta o normalidad.

Diseño de componentes de interfaz utilizando clases de Bootstrap 5 para tarjetas en grilla, tablas responsivas y alertas visuales.

Pautas de configuración para los archivos urls.py de la aplicación.

# Cambios Propios
Inserción y adaptación manual de los fragmentos de código en la estructura de directorios del proyecto dentro de VS Code.

Ajuste de nombres de variables, rutas y etiquetas {% url %} para alinearlas con la barra de navegación existente en el archivo base.html (inicio, catalogo).

Verificación y posicionamiento de los archivos estáticos y plantillas en las carpetas correspondientes exigidas por la arquitectura de Django.

# Verificación
Prueba de Servidor: Ejecución de python manage.py runserver en el entorno virtual local para validar la ausencia de errores de sintaxis y la carga correcta de los módulos de URL.

Prueba Funcional: Navegación por las secciones del sitio web para confirmar el cálculo dinámico de dispositivos por zona y la correcta lectura de los archivos JSON.

Prueba de Excepción 404: Ingreso deliberado a una ruta con un ID numérico inexistente para comprobar que el sistema intercepta el error, retorna la plantilla personalizada y emite el código de estado HTTP 404 correspondiente.