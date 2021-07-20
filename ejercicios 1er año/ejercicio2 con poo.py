#Desarrollar una clase que represente un Cuadrado y
#  tenga los siguientes métodos: inicializar el valor del 
# lado llegando como parámetro al método
#  __init__ (definir un atributo llamado lado), imprimir
#  su perímetro y su superficie.

#------------------------------------------------------------------------

class cuadrado:
    def __init__(self):
        self.lado1=int(input("ingrese la base del cuadrado: "))
        self.lado2=int(input("ingrese la altura del cuadrado: "))

    def superficie(self):
        superficie= self.lado1*self.lado2
        print("La superficie del cuadrado es: ", superficie)
    
    def perimetro(self):
        perimetro=self.lado1+self.lado2+self.lado1+self.lado2
        print("El perimetro es: ", perimetro)
        
#----------------------------------------------------------------------

cuadrado=cuadrado()
cuadrado.superficie()
cuadrado.perimetro()
