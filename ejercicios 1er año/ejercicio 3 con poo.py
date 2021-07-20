#Confeccionar una clase que administre una agenda personal. 
# Se debe almacenar el nombre de la persona, teléfono y mail
#Debe mostrar un menú con las siguientes opciones:
#1- Carga de un contacto en la agenda.
#2- Listado completo de la agenda.
#3- Consulta ingresando el nombre de la persona.
#4- Modificación de su teléfono y mail.
#5- Finalizar programa.

#------------------------------------------------------------------
import os
def limpiar():
    os.system("cls")
    print("                  bienvenido a la agenda: ")
    print("\n\nOPCIONES: \n")

def opcionm(menu):#funcion para que recive la variable menu para desplegar la opcion de volver al menu
    print("desea realizar otra operacion?: si=s  no=n")
    menu=input("opcion: ")


class agenda:
    
    def __init__(self):
        datos=[]
        menu="s"
        while menu=="s":
            limpiar()
            print("1- Carga de un contacto en la agenda.")
            print("2- Listado completo de la agenda.")
            print("3- Consulta ingresando el nombre de la persona.")
            print("4- Modificación de su teléfono y mail.")
            print("5- Finalizar programa.")
            opcion=int(input("opcion: "))

            if opcion==1:
                self.carga(datos)
                opcionm(menu)
            if opcion==2:
                self.listado()
                opcionm(menu)
            if opcion==3:
                self.consulta()
                opcionm(menu)
            if opcion==4:
                self.modificar()
                opcionm(menu)
            if opcion==5:
                break
        print("------------------Fin del programa-----------------")


    def carga(self,datos):
        op="s"
        while op=="s":
            limpiar()
            anombre=input("ingrese el nombre de la persona: ")
            tel=input("ingrese el telefono de la persona: ")
            email=input("ingrese el email: ")
            datos.append([anombre,tel,email])
            self.nombre=datos
            op=input("desea seguir cargando: ")

    def listado(self):
        limpiar()
        agendad=self.nombre
        print("La agenda queda conformada de la siguiente manera: ")
        for x in range(len(agendad)):
            print("nombre: ",agendad[x][0])
            print("tel: ",agendad[x][1])
            print("email: ", agendad[x][2])
            print("--------------------------------")
    
    def consulta(self):
        limpiar()
        agenda=self.nombre
        opconsulta="s"
        while opconsulta=="s":
            limpiar()
            consulta=input("ingrese el nombre a consultar: ")
            for x in range(len(agenda)):
                if consulta==agenda[x][0]:
                    print("nombre: ", agenda[x][0])
                    print("tel: ", agenda[x][1])
                    print("mail: ", agenda[x][2])
                else:
                    print("El nombre no existe en la agenda")
            print("Desea realizar otra consulta? s=si    n=no")
            opconsulta=input("opcion: ")

    def modificar(self):
        agenda=self.nombre
        opm="s"
        while opm=="s":
            limpiar()
            print("ingrese el nombre de la persona que quiere editar: ")
            consulta=input("nombre: ")
            for x in range(len(agenda)):
                if consulta==agenda[x][0]:
                    print("Ingrese:\n1)-Si desea modificar le telefono\n2)-Si desea modificar el mail")
                    opcioncon=int(input("opcion: "))
                    if opcioncon==1:
                        self.nombre[x][1]=input("ingrese el nuevo numero de telefono: ")
                    if opcioncon==2:
                        self.nombre[x][2]=input("ingrese la nueva direccion de mail: ")
                else:
                    print("El nombre no existe en la agenda")
                print("Desea modificar otro nombre?: s=si  n=no")
                opm=input("opcion: ")
        



agenda=agenda()