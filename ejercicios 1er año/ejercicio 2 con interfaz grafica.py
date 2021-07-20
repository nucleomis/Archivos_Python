#Mostrar dos Label, en una se muestra el nombre del programa 
# y en la segunda el año de creación.
#  Disponer un botón para finalizar el programa.
#No permitir al usuario redimensionar la ventana.

import tkinter as tk #importo al objeto de la libreria de py

import sys #importo funciones del sistema de la libreria de py

class ventana: #creo un objeto llamado ventana
    def __init__(self):# defino el atributo
        self.ventana=tk.Tk()#invoco al objeto tkinder que es una ventana
        self.ventana.title("ventana de prueba")#invoco a la funcion para definir el titulo
        self.etiqueta1=tk.Label(self.ventana,text="Facturacion")#defino una etiqueta y su texto
        self.etiqueta1.grid(column=0,row=0)#defino la ubicacion del texto de la etiqueta
        self.etiqueta2=tk.Label(self.ventana,text="2020")#defino un atributo etiqueta invocando tk.label. con el texto 2020
        self.etiqueta2.grid(column=0, row=1)#al atributo etiqueta le doy una ubicacion 
        self.boton=tk.Button(self.ventana,text="Finalizar",command=self.finalizar)#creo un atributo llamado boton
        self.boton.grid(column=0,row=2)#defino la ubicacion del boton
        self.ventana.resizable(False,False)#al objeto ventana bloqueo la opcion de redimencionar
        self.ventana.mainloop()
    
    def finalizar(self):
        sys.exit()


#---------------------------------

aplicacion=ventana()
