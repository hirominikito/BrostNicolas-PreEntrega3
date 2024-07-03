from django.urls import path
from inicio import views

urlpatterns = [
    path("", views.inicio, name="inicio"), ##### url de inicio
    path("alumnos/", views.alumnos, name="alumnos"), ###### url de muestra de alumnos y busqueda
    path("alumno/crear/", views.crear_alumno, name="crear_alumno"), ##### url de creacion de alumno
    path("alumno/eliminar/<int:id>/", views.eliminar_alumno, name="eliminar_alumno"),
    path("alumno/editar/<int:id>/", views.editar_alumno, name="editar_alumno"),
    path("alumno/<int:id>/", views.mostrar_alumno, name="mostrar_alumno"),
    
]

