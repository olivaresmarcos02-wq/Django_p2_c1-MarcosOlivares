from django.urls import path
from . import views

app_name = "dispositivos"

urlpatterns = [
path("", views.inicio, name="inicio"),
path(
    "zonas/<int:zona_id>/dispositivos/",
    views.dispositivos_zona,
    name="por_zona",
),
path(
    "numero/<int:numero_id>/dispositivos/",
    views.dispositivos_numero,
    name="por_numero",
)

]
