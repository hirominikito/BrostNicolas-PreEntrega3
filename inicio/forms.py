from django import forms


class CrearFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)