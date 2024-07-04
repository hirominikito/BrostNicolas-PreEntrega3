
from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("ingresar/", views.ingresar, name="ingresar"),
    path("salir/", LogoutView.as_view(template_name="usuarios/salir.html"), name="salir"),
    path("registro/", views.registro, name="registro"),
]
