#Confeccionar un programa con las siguientes funciones:
#1)Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores
#2)Una función que reciba como parámetro dos tuplas con los nombres y 
# sueldos de empleados y muestre el nombre del empleado con sueldo mayor.
#En el bloque principal del programa llamar dos veces a la función de carga
#  y seguidamente llamar a la función que muestra el nombre de empleado con sueldo mayor.

def carga():
    nom=input("ingrese el nombre del empleado: ")
    sueldo=float(input("ingrese el sueldo del empleado"))
    return (nom,sueldo)

def suelmayor(v1,v2):
    sueldos=v1[1],v2[1]
    mayor=sorted(sueldos)
    if v1[1]==mayor[1]:
        return v1[0]
    if v2[1]==mayor[1]:
        return v2[0]


######bloqye principal
tupla=carga()
tupla2=carga()

resultado=suelmayor(tupla,tupla2)
print("el que tiene el mayor sueldo es: ",resultado)