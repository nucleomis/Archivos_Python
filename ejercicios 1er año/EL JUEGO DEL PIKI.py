import os
def limpiar():
    os.system("cls")

limpiar()

print("                               EL JUEGO DEL PIKI!!!!:")
print("")
print("")
a=int(input("Desea leer(precione 1) o desea sumar(precione 2): "))
cont=3
continuar="si"
limpiar()

while continuar!="no":
    if a==2:
        print("Escriba el resultado")
        c=int(input("5+8= "))
        if c==13:
            print("correcto!! eres cada vez mas PIKI!!!")
        else:
            print("ERES CADA VEZ MENOS PIKI  :(")
            cont=cont-1
            print("te quedan ",cont," vidas!!" )
            continua=input("Desea continuar si o no?: ")