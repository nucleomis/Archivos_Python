#Cargar una lista con 5 elementos enteros.
#  Imprimir el mayor y un mensaje si se repite dentro de la lista
#  (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)
lista=[]
cont=0
for x in range(5):
    nombres=input("ingrese el nombre: ")
    lista.append(nombres)
nom=lista[0]
for x in range(1,5):
    if lista[x]>nom:
        nom=lista[x]
print("el nombre con mayor orden alfabetico es: ",nom)
cont=(lista.count(nom))
if cont>1:
    print ("este nombre se repite ",cont, "veces")