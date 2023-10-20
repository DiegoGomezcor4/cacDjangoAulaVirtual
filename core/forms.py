from django import forms
from django.core.exceptions import ValidationError


class ContactoForm(forms.Form):
    nombre = forms.CharField(label="nombre de contacto",required=True)
    apellido = forms.CharField(label="Apellido de contacto",required=True)
    edad = forms.IntegerField(label="Edad")
    mail = forms.EmailField(label="mail",required=True)
    mensaje = forms.CharField(widget=forms.Textarea)

    def clean_edad(self):
        if self.cleaned_data['edad'] < 18:
           raise ValidationError("el usuario no puede tener menos de 18 años")
        
        return self.cleaned_data['edad']
    
    def clean(self):
        # este if simula la busqueda en una base de datos
        if self.cleaned_data['nombre'] == 'carlos' and self.cleaned_data['apellido'] =='lopez':
            raise ValidationError('El usuario carlos lopez ya existe')
        
        # si el usuario no existe lo damos de alta  

        return self.cleaned_data