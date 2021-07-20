#Se desea saber la temperatura media trimestral de cuatro paises. 
# Para ello se tiene como dato las temperaturas medias mensuales de dichos paises.
#Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales.
#Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.
#a - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
#b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas.
#c - Calcular la temperatura media trimestral de cada país.
#c - Imprimir los nombres de los paises y las temperaturas medias trimestrales.
#b - Imprimir el nombre del pais con la temperatura media trimestral mayor.
cantpaises=(int(input("ingrese la cantidad de paises a cargar: ")))
mayoramenor=cantpaises-1
paises=[]
txpais=[]
tmediat=[]
for k in range(cantpaises):#ingreso los valores a las listas paises, 
    cont=0                #las temperaturas por trimestre y calculo el promedio por trimestre
    listan=(input("ingrese el nombre del pais: "))
    paises.append(listan)
    txpais.append([])
    tmediat.append([])
    for x in range(4):
        cont=cont+1
        print("ingrese 3 temperaturas del trimestre",cont,": ")
        listat1=int(input("ingrese temperatura : "))
        listat2=int(input("ingrese temperatura : "))
        listat3=int(input("ingrese temperatura : "))
        txpais[k].append([listat1,listat2,listat3])
        ptrim=int(listat1+listat2+listat3)/3
        tmediat[k].append(ptrim)
    

print("------------------------------------")

for x in range(cantpaises):#imprimem los paises y sus temperaturas por mes
    cont=cont+1
    print("el pais es: ",paises[x])
    print("las temperaturas medias mensuales son: ")
    print(txpais[x])
    print("---------------------------------------")

print("la temperatura media por trimestre es: ")
acum=[]
for k in range(cantpaises):#calcula la temperatura promedio trimestral
    print("pais: ",paises[k])
    cont=0#utilizo cont para imprimir a que trimestre correponde cada muestra
    acum.append([])
    for x in range(4):
        cont=cont+1
        print("trimestre ",cont,":")
        print(tmediat[k][x])
    acum[k]=(sum(tmediat[k]))/4#saco el promedio total de la temperatura por pais

for k in range(mayoramenor):
    for x in range(mayoramenor-k):
        if acum[x]>acum[x+1]:
            aux=acum[x]
            aux2=paises[x]
            acum[x]=acum[x+1]
            paises[x]=paises[x+1]
            acum[x+1]=aux
            paises[x+1]=aux2

print("------------------------------------------")
print("el pais con mayor temperatura promedio es:")
print(paises[len(paises)-1])
print("con: ", acum[len(acum)-1], "grados promedio anuales")