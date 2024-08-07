from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import FormularioCreacionUsuarios, FormularioEditarPerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import OtrosDatos

def ingresar(request):
    
    formulario = AuthenticationForm()
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get("username")
            clave = formulario.cleaned_data.get("password")
            
            user = authenticate(request, username=usuario, password=clave)

            django_login(request, user)
            
            OtrosDatos.objects.get_or_create(user=user)
            
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
    
    otrosdatos = request.user.otrosdatos
    formulario = FormularioEditarPerfil(initial={"avatar":otrosdatos.avatar},instance=request.user)
    
    if request.method == "POST":
        
        formulario = FormularioEditarPerfil(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            otrosdatos.avatar = formulario.cleaned_data.get("avatar")
            otrosdatos.save()
            formulario.save()
            return redirect("perfil")
        
    return render(request, "usuarios/editar_perfil.html", {"formulario": formulario})

class CambiarClaveUsuario(LoginRequiredMixin, PasswordChangeView):
    template_name = "usuarios/cambiar_clave.html"
    success_url = reverse_lazy("perfil")
    
def acerca_de_mi(request):

    return render(request, "usuarios/acerca_de_mi.html")

def perfil(request):
    otrosdatos = request.user.otrosdatos
    formulario = FormularioEditarPerfil(initial={"avatar":otrosdatos.avatar}, instance=request.user)
    return render(request, "usuarios/perfil.html", {"formulario": formulario})