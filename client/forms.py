from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    
    # Formulario que usa el modelo Registro y permite ingresar nombre y correo

    class Meta:
        model = Registro
        fields = ['nombre', 'correo']  # Campos que se incluirán en el formulario