#Hacer un pseudocódigo que imprima el mayor y el menor de una serie de
#cinco números,  que se introduce por teclado.
a=int(input("ingrese valor 1"))
b=int(input("ingrese valor 2"))
c=int(input("ingrese valor 3"))
d=int(input("ingrese valor 4"))
e=int(input("ingrese valor 5"))
if a>b:
    mayor=a
if a<b:
    mayor=b
if mayor<c:
    mayor=c
if mayor<d:
    mayor=d
if mayor<e:
    mayor=e
if a<b:
    menor=a
if a>b:
    menor=b
if menor>c:
    menor=c
if menor>d:
    menor=d
if menor>e:
    menor=e
print ("el numero menor es", menor)
print ("el numero mayor es", mayor)