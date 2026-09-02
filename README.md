# Django_p2_c2-MarcosOlivares
# EcoEnergy - Backend

## Descripción

Este proyecto corresponde al backend de **EcoEnergy**, desarrollado utilizando **Python y Django**.

Actualmente, el proyecto se encuentra en una etapa inicial de desarrollo. El backend ha sido recién creado y todavía no cuenta con funcionalidades, datos ni componentes de negocio implementados.

## Objetivo

El objetivo de este proyecto es desarrollar progresivamente el backend de **EcoEnergy**, estableciendo una base organizada utilizando Django para posteriormente incorporar las funcionalidades que formen parte del proyecto integrado.

## Requisitos previos

Antes de comenzar, se debe contar con:

* Python instalado.
* Git instalado.
* Un entorno de desarrollo compatible con Python, como Visual Studio Code.

> Actualmente no se especifica una versión concreta de Python, ya que todavía no está definida para el proyecto.

## Clonación del repositorio

Para obtener el proyecto, ejecutar:

```bash
git clone https://github.com/olivaresmarcos02-wq/Django_p2_c2-MarcosOlivares.git
```

Luego ingresar a la carpeta del proyecto:

```bash
cd Django_p2_c2-MarcosOlivares
```

## Creación y activación del entorno virtual

Crear el entorno virtual:

```bash
python -m venv .venv
```

### Windows

Activar el entorno virtual con:

```bash
.venv\Scripts\activate
```

### Linux / macOS

Activar el entorno virtual con:

```bash
source .venv/bin/activate
```

Una vez activado, la terminal debería mostrar que se está utilizando el entorno virtual `.venv`.

## Instalación de dependencias

El proyecto contiene actualmente un archivo `requirements.txt`, pero este se encuentra vacío.

Por lo tanto, en el estado actual no existen dependencias registradas para instalar mediante este archivo.

Cuando `requirements.txt` contenga dependencias, se podrán instalar utilizando:

```bash
pip install -r requirements.txt
```

## Comandos de verificación

Verificar que Python esté disponible:

```bash
python --version
```

Verificar que pip esté disponible:

```bash
pip --version
```

Verificar que el entorno virtual esté activo revisando la ruta del ejecutable de Python:

```bash
where python
```

En Linux / macOS:

```bash
which python
```

## Estado actual

El proyecto se encuentra en una **etapa inicial de creación**.

Actualmente:

* El repositorio está creado.
* El backend de Django se encuentra recién iniciado.
* No existen datos cargados.
* No se han implementado funcionalidades del sistema.
* El archivo `requirements.txt` existe, pero actualmente está vacío.

## Próximos pasos

Los siguientes pasos dependerán de la planificación y requerimientos del proyecto. Entre ellos se contempla continuar con la configuración y desarrollo del backend de EcoEnergy.

---

**Repositorio:**
https://github.com/olivaresmarcos02-wq/Django_p2_c2-MarcosOlivares.git

# Actualización

# Descripción actualizada

EcoEnergy es una aplicación Django que permite consultar zonas de consumo energético y el detalle de los dispositivos instalados en cada una. Los datos provienen de tres archivos JSON (no se usan Models, ORM, migraciones, CRUD, formularios ni autenticación, conforme al alcance de la Fase 1).

# Requisitos previos (versión concreta)
    -Python 3.12 o superior.
    -pip.
    -Git.

# Instalación de dependencias (real)

requirements.txt ya no está vacío. Instalar con:

```bash
pip install -r requirements.txt
```

Dependencias incluidas: Django==6.   django-bootstrap5==26.2, asgiref, sqlparse, tzdata.

# Estructura de datos
Archivo	                                Claves	                         Registros
data/zonas.json	         id, nombre, limite_kwh	                            3
data/categorias.json     id, nombre, descripcion	                        3
data/dispositivos.json	 id, nombre, consumo_kwh, zona_id, categoria_id	    8

zona_id y categoria_id referencian identificadores existentes en sus respectivos archivos. La carga se hace mediante dispositivos/services.py (cargar_json).

# Rutas funcionales
Ruta	            Nombre	                            Descripción
/	            dispositivos:inicio	                 Página de inicio.
/zonas/	        dispositivos:catalogo	             Listado de zonas con nombre, límite y cantidad de dispositivos.
/zonas/<id>/	dispositivos:detalle_zona	         Detalle de una zona: dispositivos, categoría, consumo total y estado.

# Reglas de negocio
    -Consumo total de una zona = suma de consumo_kwh de sus dispositivos.
    -Estado: ALERTA si consumo_total > limite_kwh; NORMAL en caso contrario.
    -Una zona sin dispositivos muestra "Esta zona no tiene dispositivos" sin romper la aplicación.
    -Un id de zona inexistente responde 404.

# Ejecución y pruebas realizadas
```bash
python manage.py check
python manage.py runserver
```

Escenario	                              Resultado observado
GET /	                                         200
GET /zonas/	                     200, muestra las 3 zonas
GET /zonas/1/	                                 200, consumo 390/500 → NORMAL
GET /zonas/2/	                                 200, consumo 190/150 → ALERTA
GET /zonas/99/	                                 404 controlado
python manage.py check	                         "System check identified no issues"

# Documentación adicional
    -ANALISIS.md: relaciones, multiplicidades, claves de conexión y matriz Criterio de aceptación / Archivo / Prueba.
    -IA.md: registro de uso de IA (herramienta, prompts, partes utilizadas, cambios propios y verificación).

