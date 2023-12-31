from audioop import reverse
from pyexpat.errors import messages
from typing import Any
from urllib import request
from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import redirect

from core.models import Docente


class ContactoForm(forms.Form):
    nombre = forms.CharField(label="nombre de contacto",required=True)
    apellido = forms.CharField(label="Apellido de contacto",required=True)
    edad = forms.IntegerField(label="Edad")
    dni = forms.IntegerField(label="DNI")
    mail = forms.EmailField(label="mail",required=True)
    mensaje = forms.CharField(widget=forms.Textarea)
    legajo = forms.CharField(label="legajo",required=True)

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
    
class AltaAlumnoForm(forms.Form):
    nombre = forms.CharField(label='Nobre del alumn@', required=True)
    apellido = forms.CharField(label='Apellido', required=True)
    dni = forms.IntegerField(label='DNI', required=True)
    email = forms.EmailField(label='email', required=True)
    legajo = forms.CharField(label='legago', required=True)

    # validacion en el backend  - funciona
    def clean_dni(self):
        dni = self.cleaned_data['dni']

        try:

            if (0 < dni <= 99999999):
                return dni

        except:
            messages.error(request, "el numeo de documento no puede ser negativo")
            return redirect(reverse('index'))
        

        
    
# Modelform    
class AltaDocenteModelForm(forms.ModelForm):
    class Meta:
        model = Docente 
        fields = '__all__'
    
    # validaciones    
    def clean_cuit(self):
        cuit = self.cuit.strip() # eliminar espacios en blanco al principio y al final
        
        if not cuit.isdigit():
            raise ValidationError('EL CUIT DEBE CONTENER SOLO DIGITOS')
        
        if len(cuit) != 11:
            raise ValidationError('El cuit debe tener 11 digitos')
        
        self.changed_data['cuit'] = cuit
        return self.changed_data['cuit']
    
    # validacion en el backend - no funciona
    def clean_dni(self):
        dni = self.cleaned_data['DNI']

        if dni < 0:
            raise forms.ValidationError('El DNI no puede ser negativo')

        # if not (0 < dni <= 99999999):
        #     raise forms.ValidationError('El DNI debe ser un número positivo de 8 dígitos')

        return dni
        