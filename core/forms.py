from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="nombre de contacto",required=True)
    apellido = forms.CharField(label="Apellido de contacto",required=True)
    mail = forms.EmailField(label="mail",required=True)
    mensaje = forms.Textarea("dejanos tu comentario")