#Definir una lista que almacene por asignación los nombres de 5 personas.
# Contar cuantos de esos nombres tienen 5 o más caracteres.
nombres=[]
for x in range(5):
    lista=(input("ingrese un nombre: "))
    nombres.append(lista)
cont=0
for x in range(len(nombres)):
    if len(nombres[x])>5:
        cont=cont+1
print("---------------------------------")
print("los nombres con mas de 5 caracteres son: ",cont)