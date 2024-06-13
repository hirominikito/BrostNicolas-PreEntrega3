from django.shortcuts import render, redirect

def inicio(request):
    return render(request, "inicio/inicio.html")


#### CREACION DE LA VISTA DE LO QUE ESTOY CREANDOOOOOOOOOOOOOOOOOOOO

from inicio.forms import (CrearFormulario)

def crearAlumno(request):

    print("valor de la request: ", request)
    print("valor de GET: ", request.GET)
    print("valor de post: ", request.POST)    
    
    formulario == CrearFormulario()
    
    if request.method == "POST":
        formulario == CrearFormulario(request.POST)
            
        if formulario.is_valid():
            datos = formulario.cleaned_data
            alumno = Alumno(nombre=datos.get("nombre"), apellido=datos.get("apellido"))
            alumno.save()
            return redirect("autos")
    
    return render(request, "inicio/NOMBRE DE LA APP DENTRO DE TEMPLATE INICIO.html", {"formulario": formulario})
    
def alumnos(request):
    
    alumnos = Alumno.objects.all()
    
    return render(request, "inicio/alumnos.html", {"alumnos": alumnos})
    
    
    