#Realizar un programa de carga, según  diseño Fig 7, los archivos maestro
#  (clientes, artículos) ya poseen datos grabados en el disco rígido. 
#Proceso: 

#1) Ingresar la clave cliente, si es cero sale del programa, si no verificar si existe, en caso que no exista, mensaje: "no puede comprar porque no existe". caso contrario, se accede al archivo maestro de cliente y se imprime en pantalla el nombre y apellido.

#2) Se ingresa el numero de factura y la fecha. 

#3) Se ingresa el código de artículo, se verifica en archivo, en caso de que no exista, mensaje "no existe artículo, reingrese". Caso contrario se imprime en pantalla el detalle del artículo. 

#4) Se ingresa  el importe a pagar


#4) Se solicita 1 Grabar 2- cancelar (en el caso de grabar se genera el archivo de novedad según diseño Fig 3) .


#Figura 7 
#Pantalla de carga
#Cód. Cliente:xxx
#Nya: ZZZZZZZ
#Nro. De Factura: xxxxxx	Fecha: xx/xx/xx
#Cód. Artículo	Descripción Artículo 	Importe
#xxxx	zzzzzz	xxxxx
#1 - Graba	2- Cancela


archivo=open("lista.txt","r")
cont=len(archivo.readlines())
print(cont)