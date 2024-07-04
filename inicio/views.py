from django.shortcuts import render, redirect


def inicio(request):
    return render(request, "inicio/inicio.html")

from django.http import HttpResponse
from django.template import Template, Context, loader


from inicio.forms import CrearAlumnoFormulario, BuscarAlumno, EditarAlumnoFormulario
from inicio.models import Alumno
from django.contrib.auth.decorators import login_required

def crear_alumno(request):

    print("valor de la request: ", request)
    print("valor de GET: ", request.GET)
    print("valor de post: ", request.POST)    
    
    formulario = CrearAlumnoFormulario()
    
    if request.method == "POST":
        formulario = CrearAlumnoFormulario(request.POST)
            
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
        alumnos = Alumno.objects.filter(apellido__icontains=apellido)
    
    return render(request, "inicio/alumnos.html", {"alumnos": alumnos, "formulario": formulario})

@login_required
def eliminar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    return redirect("alumnos")

@login_required
def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    
    formulario = EditarAlumnoFormulario(initial={"apellido": alumno.apellido, "nombre": alumno.nombre})
    
    if request.method == "POST":
        formulario = EditarAlumnoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            alumno.apellido = info["apellido"]
            alumno.nombre = info["nombre"]
            alumno.save()
            return redirect("alumnos")
    
    return render(request, "inicio/editar_alumno.html", {"formulario": formulario, "alumno": alumno})

def mostrar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)

    return render(request, "inicio/mostrar_alumno.html", {"alumno": alumno})
    
    
    