#Declarar una clase Cuenta y dos subclases CajaAhorra y PlazoFijo.
#  Definir los atributos y métodos comunes entre una caja de ahorro 
# y un plazo fijo y agruparlos en la clase Cuenta.
#Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. 
# Un plazo fijo añade un plazo de imposición en días y una tasa de interés. 
# Hacer que la caja de ahorro no genera intereses.
#En el bloque principal del programa definir un objeto de la clase 
# CajaAhorro y otro de la clase PlazoFijo.
import os#importo las funciones del diccionario de python

def limpiar(): #designo una funcion para invocar al clear de consola
    os.system("cls")


class cuenta: #creo una clase padre que contiene caracteristicas en comun con las subfunciones
    def __init__(self):
        self.nombre=input("ingrese el nombre del cliente: ")
        self.monto=float(input("ingrese el monto: "))
    
    def imprimir(self):
        print("el nombre es: ",self.nombre)
        print("el monto es: ",self.monto)

class caja_ahorro(cuenta):#creo una subclase con la clase padre cuenta
    def __init__(self):
        super().__init__()#invoco el metodo __init__ de la clase padre
    
    def impresion(self):
        super().imprimir()#invoco el metodo impresion de la clase padre

class plazo_fijo(cuenta):#creo una subclase llamada plazo fijo
    def __init__(self):
        super().__init__()#invoco el metodo __init__ de la clase padre
        self.plazo=input("ingrese el plazo: ")#agrego metodos unicos de esta clase
        self.interes=float(input("ingrese el interes: "))
    def operacion(self):
        self.total=self.monto+self.interes
    def imp(self):
        super().imprimir()
        print("el plazo es: ", self.plazo)
        print("el interes es: ", self.total)
#-------------------------------------------------------
op="s"
while op=="s":
    limpiar()
    print("creacion de cuenta: ")
    print("desea crear una caja de ahorro?presione 1\ndesea crear un plazo fijo? presione 2")
    select=int(input("opcion: "))
    if select==1:
        limpiar()
        print("creacion de cuenta como caja de ahorro: ")
        caja=caja_ahorro()
        caja.impresion()
    if select==2:
        limpiar()
        print("creacion de cuenta como plazo fijo: ")
        plazo=plazo_fijo()
        plazo.operacion()
        plazo.imp()
    op=input("desea realizar optra operacion?s/n: ")











