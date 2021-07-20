#En un curso de 4 alumnos se registraron las notas de sus exámenes
#  y se deben procesar de acuerdo a lo siguiente:
#a) Ingresar nombre y nota de cada alumno 
# (almacenar los datos en dos listas paralelas)
#b) Realizar un listado que muestre los nombres, notas y condición del alumno.
#  En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8,
#  "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente"
#  si la nota es inferior a 4.
#c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.
alumnos=[]
notas=[]
cont=0
for x in range(5):
    nomalumnos=input("ingrese el nombre de los alumnos: ")
    alumnos.append(nomalumnos)
    nomnotas=int(input("ingrese la nota del alumno: "))
    notas.append(nomalumnos)
    if nomnotas>=8:
        print("condicion: muy bueno")
        cont=cont+1
    if nomnotas<8 and nomnotas>4:
        print("condicion: bueno")
    if nomnotas<=4:
        print("condicion: insuficiente")
print("la cantidad de alumnos que superan el 8 son: ",cont)