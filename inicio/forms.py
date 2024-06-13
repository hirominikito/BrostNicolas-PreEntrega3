from django import forms


class CrearFormulario(forms.FORM):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)