#Crear un diccionario en Python que defina como clave el número 
# de documento de una persona y como valor un string con su nombre.
#Desarrollar las siguientes funciones:
#1) Cargar por teclado los datos de 4 personas.
#2) Listado completo del diccionario.
#3) Consulta del nombre de una persona ingresando su número de documento.

def base():
    cont=0
    datos={}
    while cont!=4:
        cont=cont+1
        nombre=input("ingrese el nombre de la persona: ")
        dni=int(input("ingrese el numero de documento: "))
        datos[dni]=nombre
    return datos

def busqueda(dic):
    opcion="s"
    while opcion=="s":
        busc=int(input("ingrese la dni de la persona: "))
        print("resultado:\n",dic[busc])
        opcion=input("desea realizar otra busqueda?:\ns: si--n: no: ")

#--------------------------------------------------------------------    

diccionario=base()
print("el diccionario queda conformado de la siguiente forma: ")

for dni in diccionario:
    print("dni: ",dni,"nombre: ",diccionario[dni])

busqueda(diccionario)