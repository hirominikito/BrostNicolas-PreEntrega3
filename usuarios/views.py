from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from usuarios.forms import FormularioCreacionUsuarios, FormularioEditarPerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

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
        if formulario.is_valid():
            formulario.save()
            return redirect("ingresar")
   
    return render(request, "usuarios/registro.html", {"formulario": formulario})

@login_required
def editar_perfil(request):
    formulario = FormularioEditarPerfil(instance=request.user)
    
    if request.method == "POST":
        formulario = FormularioEditarPerfil(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            return redirect("editar_perfil")
    return render(request, "usuarios/editar_perfil.html", {"formulario": formulario})

class CambiarClaveUsuario(PasswordChangeView):
    template_name = "usuarios/cambiar_clave.html"
    sucess_url = reverse_lazy("editar_perfil")