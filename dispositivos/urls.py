from django.urls import path
from . import views

app_name = "dispositivos"

urlpatterns = [
path("", views.inicio, name="inicio"),


path('dispositivos/catalogo/', views.catalogo, name='catalogo'),
path('zonas/<int:zona_id>/', views.detalle_zona_view, name='detalle_zona'),


]
