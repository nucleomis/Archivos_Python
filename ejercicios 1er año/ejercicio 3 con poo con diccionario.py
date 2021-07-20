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
    print("                  Bienvenido a la agenda: ")
    print("\n\nOPCIONES: \n")

def opcionm(menu):#funcion para que recive la variable menu para desplegar la opcion de volver al menu
    print("desea realizar otra operacion?: si=s  no=n")
    menu=input("opcion: ")


class agenda:
    
    def __init__(self):
        self.nombre={}
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
                self.carga()
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


    def carga(self):
        op="s"
        while op=="s":
            datos=[]
            limpiar()
            anombre=input("ingrese el nombre de la persona: ")
            tel=input("ingrese el telefono de la persona: ")
            datos.append(tel)
            email=input("ingrese el email: ")
            datos.append(email)
            self.nombre[anombre]=datos
            op=input("desea seguir cargando: ")

    def listado(self):
        limpiar()
        agendad=self.nombre
        print("La agenda queda conformada de la siguiente manera: ")
        for consulta in agendad:
            print("nombre: ",consulta)
            print("tel: ", agendad[consulta][0])
            print("email: ", agendad[consulta][1])
            print("--------------------------------")
    
    def consulta(self):
        limpiar()
        agenda=self.nombre
        opconsulta="s"
        while opconsulta=="s":
            limpiar()
            consulta=input("ingrese el nombre a consultar: ")
            if consulta in agenda:
                print("nombre: ", consulta)
                print("tel: ", agenda[consulta][0])
                print("mail: ", agenda[consulta][1])
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
            if consulta in agenda:
                print("Ingrese:\n1)-Si desea modificar le telefono\n2)-Si desea modificar el mail")
                opcioncon=int(input("opcion: "))
                if opcioncon==1:
                    self.nombre[consulta][0]=input("ingrese el nuevo numero de telefono: ")
                if opcioncon==2:
                    self.nombre[consulta][1]=input("ingrese la nueva direccion de mail: ")
            else:
                print("El nombre no existe en la agenda")
            print("Desea modificar otro nombre?: s=si  n=no")
            opm=input("opcion: ")
        



agenda=agenda()