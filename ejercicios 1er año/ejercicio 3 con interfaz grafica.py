#Disponer dos objetos de la clase Button con las etiquetas:
#  "varón" y "mujer", al presionarse mostrar en la barra de 
# títulos de la ventana la etiqueta del botón presionado.
import tkinter as tk
import sys


class ventana:
    def __init__(self):
        self.valor=" "
        self.ventana=tk.Tk()
        self.ventana.title("Tarea")
        self.etiqueta1=tk.Label(self.ventana,text="valor: ")
        self.etiqueta1.grid(column=0, row=0)
        self.etiqueta_valor=tk.Label(self.ventana,text=self.valor)
        self.etiqueta_valor.grid(column=4,row=0)

        self.boton1=tk.Button(self.ventana,text="varon",command=self.accion1)
        self.boton1.grid(column=0,row=2)


        self.boton2=tk.Button(self.ventana,text="mujer",command=self.accion2)
        self.boton2.grid(column=0,row=3)

        self.boton3=tk.Button(self.ventana,text="salir",command=self.salir)
        self.boton3.grid(column=3,row=4)

        self.ventana.mainloop()

    def accion1(self):
        self.valor="varon"
        self.etiqueta_valor.config(text=self.valor)

    def accion2(self):
        self.valor="mujer"
        self.etiqueta_valor.config(text=self.valor)

    def salir(self):
        sys.exit()


aplicacion=ventana()