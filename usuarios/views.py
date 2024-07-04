from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from usuarios.forms import FormularioCreacionUsuarios

def ingresar(request):
    
    formulario = AuthenticationForm()
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get("username")
            clave = formulario.cleaned_data.get("password")
            
            usuario = authenticate(username=usuario, password=clave)

            login(request, usuario)
            return redirect("inicio")
    
    return render(request, "usuarios/ingresar.html", {"formulario": formulario})

def registro(request):
    formulario = FormularioCreacionUsuarios()
    
    if request.method == "POST":
        formulario = FormularioCreacionUsuarios(request.POST)
        if formulario.is_valid:
            formulario.save()
            return redirect("ingresar")
   
    return render(request, "usuarios/registro.html", {"formulario": formulario})