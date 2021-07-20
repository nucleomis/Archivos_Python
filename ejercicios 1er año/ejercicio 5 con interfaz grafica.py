#Mostrar los botones del 1 al 5. Cuando se presiona mostrar en una Label
#todos los botones presionados hasta ese momento.


import tkinter as tk


class ventana:
    def __init__(self):
        self.valor=[]
        self.ventana=tk.Tk()
        self.ventana.title("tarea 5")
        self.etiqueta=tk.Label(self.ventana,text=self.valor)
        self.etiqueta.grid(column=0, row=0)

        self.boton1=tk.Button(self.ventana,text="numero 1",command=self.add1)
        self.boton1.grid(column=0,row=1)

        self.boton2=tk.Button(self.ventana,text="numero 2",command=self.add2)
        self.boton2.grid(column=0,row=2)

        self.boton3=tk.Button(self.ventana,text="numero 3",command=self.add3)
        self.boton3.grid(column=0,row=3)

        self.boton4=tk.Button(self.ventana,text="numero 4",command=self.add4)
        self.boton4.grid(column=0,row=4)

        self.boton5=tk.Button(self.ventana,text="numero 5",command=self.add5)
        self.boton5.grid(column=0,row=5)

        self.boton6=tk.Button(self.ventana, text="Resta", command=self.res)
        self.boton6.grid(column=0,row=6)

        self.ventana.mainloop()


    def add1(self):
        val="1"
        self.valor.append(val)
        self.etiqueta.config(text=self.valor)

    def add2(self):
        val="2"
        self.valor.append(val)
        self.etiqueta.config(text=self.valor)

    def add3(self):
        val="3"
        self.valor.append(val)
        self.etiqueta.config(text=self.valor)

    def add4(self):
        val="4"
        self.valor.append(val)
        self.etiqueta.config(text=self.valor)

    def add5(self):
        val="5"
        self.valor.append(val)
        self.etiqueta.config(text=self.valor)

    def res(self):
        longitud=len(self.valor)-1
        self.valor.pop(longitud)
        self.etiqueta.config(text=self.valor)


aplicacion=ventana()