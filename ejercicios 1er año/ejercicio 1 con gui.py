#Mostrar una ventana y que en su título aparezca el mensaje 'Hola Mundo'.
#El programa en Python haciendo uso del módulo 'tkinter' requiere el
#  siguiente algoritmo:

import tkinter as tk


class ventana:
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("hola todos")
        self.ventana.mainloop()




vent=ventana()