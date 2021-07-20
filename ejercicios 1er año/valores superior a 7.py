#Definir una lista por asignación con 5 enteros.
#  Mostrar por pantalla solo los elementos con valor iguales o superiores a 7
a=int(input("ingrese un valor: "))
b=int(input("ingrese un valor 2: "))
c=int(input("ingrese un valor 3: "))
d=int(input("ingrese un valor 4: "))
e=int(input("ingrese un valor 5: "))
x=0
valores=a,b,c,d,e
while x<len(valores):
    if valores[x]>7:
        print(valores[x])
    x=x+1