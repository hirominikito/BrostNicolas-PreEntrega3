from django import forms



class CrearFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    fecha = forms.DateField(required=False)
    edad = forms.IntegerField() 
    
class CrearAlumnoFormulario(CrearFormulario):
    ...

class EditarAlumnoFormulario(CrearFormulario):
    ...


class BuscarAlumno(forms.Form):
    apellido = forms.CharField(max_length=20, required=False)
    
