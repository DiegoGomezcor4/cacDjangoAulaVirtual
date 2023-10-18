from django import forms

class BlueBackgroundTextInput(forms.TextInput):
    class Media:
        CSS = {'all': ('core/css/blue_background_text_input.css',)}

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="nombre de contacto", widget=forms.TextInput(attrs={'class': 'fondo_rojo'}),required=True)
    apellido = forms.CharField(label="Apellido de contacto",widget=BlueBackgroundTextInput,required=True)
    mail = forms.EmailField(label="mail",required=True)
    mensaje = forms.CharField(widget=forms.Textarea)
    fecha = forms.DateField()