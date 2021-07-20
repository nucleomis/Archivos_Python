#Confeccionar un programa que permita ingresar dos números 
# en controles de tipo Entry, luego sumar los dos valores 
# ingresados y mostrar la suma en una Label al presionar un botón.

import tkinter as tk



class  ventana:
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("suma de numeros")
        self.etiqueta1=tk.Label(self.ventana,text="ingrese el valor: ")
        self.etiqueta1.grid(column=0,row=2)
        self.valor1=tk.StringVar()
        self.ingreso1=tk.Entry(self.ventana,width=20,textvariable=self.valor1)
        self.ingreso1.grid(column=2,row=2)
        self.etiqueta2=tk.Label(self.ventana,text="ingrese segundo valor: ")
        self.etiqueta2.grid(column=0,row=5)
        self.valor2=tk.StringVar()
        self.ingreso2=tk.Entry(self.ventana,width=20,textvariable=self.valor2)
        self.ingreso2.grid(column=2,row=5)
        self.boton_calcular=tk.Button(self.ventana,text="Sumar",command=self.operacion)
        self.boton_calcular.grid(column=2,row=7)
        self.etiqueta3=tk.Label(self.ventana,text="El resultado es: ")
        self.etiqueta3.grid(column=1,row=8)
        self.ventana.mainloop()


    
    def operacion(self):#funcion u atributo que realiza la suma
        valor1=int(self.ingreso1.get())
        valor2=int(self.ingreso2.get())
        self.suma=valor1+valor2
        self.resultado=str(self.suma)
        self.etiqueta3.configure(text=str("El resultado es: "+self.resultado))


aplicacion=ventana()