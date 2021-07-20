#Elaborar una función que reciba tres enteros
#  y nos retorne el valor promedio de los mismos.

def promedio(v1,v2,v3):
    calc=(v1+v2+v3)/3
    return calc

linea1=int(input("ingrese el valor"))
linea2=int(input("ingrese el valor"))
linea3=int(input("ingrese el valor"))
resultado=promedio(linea1,linea2,linea3)

print(resultado)