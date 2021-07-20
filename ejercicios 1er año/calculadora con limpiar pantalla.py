import os
 
#entro en el bucle
salir = False
# evaluo la condicion si la variable salir es verdadera entonces entro al bucle
# el operador (not) invierte el valor de la variable
while not salir:
 
    print ('CALCULADORA')
 
    print() #espacio libre
 
    print ('Menu Principal')
 
    print #espacio libre
 
    print ('1 - Sumr')
    print ('2 - Restar')
    print ('3 - Multiplicar')
    print ('4 - Dividir')
    print ('0 - Salir')
 
    print #espacio libre
 
    op =input('Opcion: ')
 
    print #espacio libre
 
    if op == str(1):
        n1=float(input('Numero 1: '))
        n2=float(input('Numero 2: '))
        print ('la suma de', n1,' y', n2,' es: ',n1+n2,'>>>',input('Enter para continuar')
 
 
    if op==str(0): # cambio el valor de salir a verdadero
        salir=True
 
    os.system('cls')
    print #espacio libre
 
raw_input('Gracias por usar mi calculadora
Enter para finalizar') # esta linea permite que el programa no termine hasta que se de Enter