#Crear un diccionario en Python para almacenar los datos de empleados de una empresa. 
# La clave será su número de legajo y en su valor almacenar una lista con el nombre, 
# profesión y sueldo.
#Desarrollar las siguientes funciones:
#1) Carga de datos de empleados.
#2) Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo para buscarlo.
#3) Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"

def carga():
    diccionario={}
    op="s"
    datos=[]
    while op=="s":
        legajo=int(input("ingrese el numero de legajo: "))
        nombre=input("ingrese el nombre del empleado: ")
        profesión=input("ingrese la profesion: ")
        sueldo=float(input("ingrese el sueldo: "))
        datos.append(nombre)
        datos.append(profesión)
        datos.append(sueldo)
        diccionario[legajo]=datos
        op=input("desea seguir cargando empleados?: ")
    return diccionario

def consulta(diccionario):
    consulta=int(input("ingrese el numero de legajo: "))
    for consulta in diccionario:
        if consulta in diccionario:
            print("el sueldo actual es de: ", diccionario[consulta][2],"\n")
            modificar=float(input("ingrese el sueldo para modificar: "))
            diccionario[consulta][2]=modificar
    return consulta



dicc=carga()

consulta(dicc)

for consulta in dicc:
    print("el sueldo de: ",dicc[consulta][0],"ahora es de: ",dicc[consulta][2])