linea1=input("ingrese un nombre")
linea2=input("ingrese otro nombre")
linea3=input("ingrese otro nombre")

arch=open("lista.txt","w")
arch.write(linea1)
arch.write("\n")
arch.write(linea2)
arch.write("\n")
arch.write(linea3)
arch.write("\n")
arch.close()

arch=open("lista.txt","r")
listas=arch.readlines()
print("lectura del archivo")
for x in listas:
    print(x, end="")
arch.close()
print("fin de la lista")

print("agregamos nuevo cotenido")

arch=open("lista.txt","a")
arch.write("nuevo1\n")
arch.write("nuevo2\n")
arch.write("nuevo3\n")
arch.close()

arch=open("lista.txt", "r")
lista=arch.read()
print(lista)
arch.close()
