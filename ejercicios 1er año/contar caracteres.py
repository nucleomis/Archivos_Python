#Definir una lista que almacene por asignación los nombres de 5 personas.
#  Contar cuantos de esos nombres tienen 5 o más caracteres.
nom1=input("ingrese un nombre: ")
nom2=input("ingrese otro nombre: ")
nom3=input("ingrese otro nombre: ")
nom4=input("ingrese otro nombre: ")
nom5=input("ingrese otro nombre: ")
x=0
if len(nom1)>=5:
    x=x+1
if len(nom2)>=5:
    x=x+1
if len(nom3)>=5:
    x=x+1
if len(nom4)>=5:
    x=x+1
if len(nom5)>=5:
    x=x+1
print("hay", x, "nombres que tienen mas de 5 caracteres")    