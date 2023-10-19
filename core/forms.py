from typing import Any
from django import forms
from django.core.exceptions import ValidationError


class ContactoForm(forms.Form):
    nombre = forms.CharField(label="nombre de contacto", widget=forms.TextInput(attrs={'class': 'fondo_rojo'}),required=True)
    apellido = forms.CharField(label="Apellido de contacto",required=True)
    edad = forms.CharField(label="Edad")
    mail = forms.EmailField(label="mail",required=True)
    mensaje = forms.CharField(widget=forms.Textarea)

    def clean_edad(self):
        if self.cleaned_data['edad'] < 18:
            ValidationError("el usuario no puede tener menos de 18 años")
        
        return self.cleaned_data["edad"]
    
    def clean(self):
        pass