#Confeccionar una clase que permita carga el nombre y la edad de una persona.
#  Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)

class alumno:
    def persona (self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    def mayor(self):
        if self.edad>=18:
            print ("el de mayor edad es", self.nombre, self.edad)

    def imprimir(self):
        print(self.nombre, self.edad)
        


tipo1=alumno()
tipo1.persona("pedro",16)
tipo1.imprimir()
tipo1.mayor()


tipo2=alumno()
tipo2.persona("antonio",22)
tipo2.imprimir()
tipo2.mayor()


