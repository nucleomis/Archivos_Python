from django import forms
# Create your models here.

class Formulario(forms.Form):
    nombre = forms.CharField(label = 'nombre', max_length=50, required=True)
    email = forms.EmailField(label='email', max_length=30, required=True)
    asunto = forms.CharField(label='asunto', max_length=20 , required=True)
    mensaje = forms.CharField(label='mensaje',widget=forms.Textarea, required=True)