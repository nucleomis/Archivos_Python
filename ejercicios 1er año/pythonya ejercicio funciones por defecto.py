#Confeccionar una función que reciba entre 2 y 5 
# enteros. La misma nos debe retornar la suma de dichos valores.
#  Debe tener tres parámetros por defecto.

def suma_valores(lista,def1="-",salud="fin"):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
        print(suma)
        print(def1*suma)
        print(salud)

param=[]
while len(param)<5:
    ing=int(input("ingrese un numero: "))
    param.append(ing)
subr=input("ingrese un simbolo: ")
frase=input("ingrese una frase: ")
suma_valores(param,subr,frase)