from django import forms


class Contacto(forms.Form):
    nombre = forms.CharField(label="Contacto")
    apellido = forms.ChoiceField(label="Apellido de contacto")
    email = forms.EmailField()
