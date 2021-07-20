# Elaborar una función que muestre la tabla de multiplicar del valor 
# que le enviemos como parámetro. Definir un segundo parámetro llamado 
# termino que por defecto almacene el valor 10. 
# Se deben mostrar tantos términos de la tabla de multiplicar como lo indica el segundo parámetro.
#Llamar a la función desde el bloque principal de nuestro programa con argumentos nombrados.

def tabla(v1,v2=int(input("ingrese un el limite de la tabla: "))):
    cont2=0
    while cont2<=v2:
        cont2+=1
        multi=v1*cont2
        print(v1,"x",cont2,"=",multi)


g=int(input("ingrese un numero para saber su tabla: "))
tabla(g)         







#la forma que mas me gusto!
#def tabla(v1):
#    cont2=0
#    while cont2<10:
#        cont2=cont2+1
#        mult=v1*cont2
#        print(v1,"x",cont2,"=",mult)
#    lista=[]
#    if cont2==10:
#        mult
#        for x in range(1, mult+1):
#           cont=x
#           lista.append(cont)
#    print(lista)

#g=int(input("ingrese un numero para saber su tabla: "))
#tabla(g)         