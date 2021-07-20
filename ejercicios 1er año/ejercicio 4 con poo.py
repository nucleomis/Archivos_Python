#Plantear una clase Club y otra clase Socio.
#La clase Socio debe tener los siguientes atributos: nombre y la antigüedad
#  en el club (en años).
#En el método __init__ de la clase Socio pedir la carga por teclado 
# del nombre y su antigüedad.
#La clase Club debe tener como atributos 3 objetos de la clase Socio.
#Definir una responsabilidad para imprimir el nombre del socio
#  con mayor antigüedad en el club.

class socio:
    def __init__(self):
        self.nombre=input("ingrese el nonmbre del socio: ")
        self.anti=int(input("ingrese la antiguedad del empleado: "))

    def imprimir(self):
        print(self.nombre," tiene una antiguedad de: ",self.anti)
    
    def ret_nombre(self):
        return self.nombre

    def ret_antiguedad(self):
        return self.anti


class club:
    def __init__(self):
        self.socio1=socio()
        self.socio2=socio()
        self.socio3=socio()
    def cargo(self):
        if self.socio1.ret_antiguedad()>self.socio2.ret_antiguedad() and self.socio1.ret_antiguedad()>self.socio3.ret_antiguedad():
            print("el socio mas antiguo es: ", self.socio1.ret_nombre())
        else:
            if self.socio2.ret_antiguedad()>self.socio3.ret_antiguedad():
                print("el socio mas antiguo es: ", self.socio2.ret_nombre())
            else:
                print("el socio mas antiguo es: ", self.socio3.ret_nombre())
        
                
        


pro=club()
pro.cargo()