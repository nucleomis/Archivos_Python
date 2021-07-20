#Ingresar el nombre de usuario y clave en controles de tipo Entry. 
# Si se ingresa las cadena (usuario: juan, clave="abc123")
#  luego mostrar en el título de la ventana el mensaje "Correcto" 
# en caso contrario mostrar el mensaje "Incorrecto".
#Para mostrar '*' cuando se ingresa la clave debemos pasar 
# en el parámetro 'show' el caracter a mostrar:

import tkinter as tk

class ventana:
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("panel de usuario")
        self.etiqueta=tk.Label(text="ingreso de usuario")
        self.etiqueta.grid(column=0,row=0)
        self.dato1=tk.StringVar()
        self.etiqueta1=tk.Label(text="ingrese el usuario: ")
        self.etiqueta1.grid(column=0,row=1)
        self.entrada1=tk.Entry(self.ventana,width=20,textvariable=self.dato1)
        self.entrada1.grid(column=1,row=1)
        self.dato2=tk.StringVar()
        self.etiqueta2=tk.Label(text="ingrese la contraseña: ")
        self.etiqueta2.grid(column=0,row=3)        
        self.entrada2=tk.Entry(self.ventana,width=20,textvariable=self.dato2,show="*")
        self.entrada2.grid(column=1,row=3)
        self.boton=tk.Button(self.ventana,text="comprobar",command=self.comprobar)
        self.boton.grid(column=1,row=5)
        self.etiqueta3=tk.Label(text="")
        self.etiqueta3.grid(column=1,row=4)
        self.ventana.mainloop()

    def comprobar(self):
        nombre="juan"
        contraseña="abc123"
        self.nombre=str(self.dato1.get())
        self.password=str(self.dato2.get())
        if self.nombre==nombre and self.password==contraseña:
            self.etiqueta3.config(text="los datos son correctos")
        else:
            self.etiqueta3.config(text="el usuario o la contraseña no son correctos")                     

vent=ventana()