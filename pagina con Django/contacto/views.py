from django.db import models
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from tiendaonline import settings
from . import forms
# Create your views here.

def contacto(request):
    formulario = forms.Formulario()

    if request.method == "POST":

        formulario = forms.Formulario(data=request.POST) #en esta variable cargo los datos del post
        #con data= request.POST dentro de la clase Formulario()

        if formulario.is_valid():#verifico que el formulario este correctamente rellenado

            nombre = request.POST["nombre"]+" "+request.POST["email"]

            asunto = request.POST["asunto"]

            mensaje = request.POST["mensaje"]

            #correo_emisor = settings.EMAIL_HOST_USER

            try:
            
                send_mail(asunto, f"el usuario {nombre} escribio el siguiente mensaje:\n {mensaje}", request.POST["email"],['nucleo.mis@gmail.com'])

                return redirect("/contacto/?enviado") #redirect sirve para enviarme a otra pagina que le asigno como parametro
            except:

                return redirect("/contacto/?fallo")#en caso de que falle el envio de correo

    return render(request,"contacto.html", {"formulario": formulario})
