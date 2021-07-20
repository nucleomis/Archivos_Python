#Realizar un programa que pida la carga de dos listas numéricas enteras 
# de 4 elementos cada una. Generar una tercer lista que surja de la suma 
# de los elementos de la misma posición de cada lista.
#  Mostrar esta tercer lista.
lista1=[]
lista2=[]
suma=0
lista3=[]
for x in range(4):
    inlista1=int(input("ingrese el valor a sumar: "))
    lista1.append(inlista1)
    inlista2=int(input("ingrese el otro valor a sumar: "))
    lista2.append(inlista2)
    suma=inlista1+inlista2
    lista3.append(suma)
print("el resultado de las sumas son: ",lista3)
    