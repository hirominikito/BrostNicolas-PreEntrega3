from django.shortcuts import render, redirect


def inicio(request):
    return render(request, "inicio/inicio.html")

from django.http import HttpResponse
from django.template import Template, Context, loader


from inicio.forms import CrearFormulario, BuscarAlumno
from inicio.models import Alumno

def crearAlumno(request):

    print("valor de la request: ", request)
    print("valor de GET: ", request.GET)
    print("valor de post: ", request.POST)    
    
    formulario = CrearFormulario()
    
    if request.method == "POST":
        formulario = CrearFormulario(request.POST)
            
        if formulario.is_valid():
            datos = formulario.cleaned_data
            alumno = Alumno(nombre=datos.get("nombre"), apellido=datos.get("apellido"))
            alumno.save()
            return redirect("alumnos")

    
    return render(request, "inicio/crear_alumno.html", {"formulario": formulario})
    
def alumnos(request):
    
    formulario = BuscarAlumno(request.GET)
    if formulario.is_valid():   
        apellido = formulario.cleaned_data["apellido"]
        alumnos = Alumno.objects.filter(apellido=apellido)
    
    alumnos = Alumno.objects.all()
    
    return render(request, "inicio/alumnos.html", {"alumnos": alumnos, "formulario": formulario})
    
    