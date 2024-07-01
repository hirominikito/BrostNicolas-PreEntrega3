from django.urls import path
from inicio import views

urlpatterns = [
    path("", views.inicio, name="inicio"), ##### url de inicio
    path("alumnos/", views.alumnos, name="alumnos"), ###### url de muestra de alumnos
    path("alumno/crear/", views.crearAlumno, name="crearAlumno"), ##### url de creacion de alumno
    
]

