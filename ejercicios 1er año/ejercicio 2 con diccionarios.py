#Se desea almacenar los datos de 3 alumnos. 
# Definir un diccionario cuya clave sea el número de documento del alumno. 
# Como valor almacenar una lista con componentes de tipo tupla donde almacenamos
#  nombre de materia y su nota.

#Crear las siguientes funciones:
#1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
#2) Listado de todos los alumnos con sus notas
#3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.

#-----------------------------------------------------------------------------------
def carga():#funcion de carga
    cont=0
    datos_alumnos={}#creo la variable de tipo diccionario
    while cont!=3:
        cont=cont+1# contador de cantidad de alumnos a cargar
        dni=int(input("ingrese el numero de dni: "))               
        nombrea=input("ingrese el nombre del alumno: ")
        op="s"
        materia=[] #variable tipo lista para la carga de las materias y las notas
        while op=="s": #condicion mientras se cumpla continuara la carga
            listaM=input("ingrese el nombre de la materia: ")#variable del nombre de la materia
            nota=int(input("ingrese la nota de la materia: "))#variable de nota de la materia
            materia.append((listaM,nota))#agregamos a la variable lista, las materias y notas de alumno
            op=input("desea seguir cargando materia y nota?: ")# consulta para modificar el valor de op para continuar o no la carga
        datos_alumnos[dni]=nombrea,materia#creacion del diccionario teniendo como indice el dni del alumno
    return datos_alumnos

def listado(datoAlumnos): # funcion que tiene como parametro una variable para analizar
    print("El listado queda conformado de la siguiente manera: ")
    for dni in datoAlumnos: # con este for dni itera y obtiene el valor del dni mientras va recorriendo la variable tipo diccionario
        print("dni:",dni,"nombre:",datoAlumnos[dni][0])#imprime el valor obtenido, en este caso el dni y tambien imprime el nombre del alumno usando el valor dni como referencia para la ubicaicon
        for materias in datoAlumnos[dni][1]:# en el diccionario, en la ubicacion de la lista de materia, recorremos la misma con la variable materias
            print(materias[0],materias[1]) #dentro de la lista de materias, recorreomos e imprimimos la ubicacion del nombre materia y la nota

def consulta(busqueda): #variable con la cual la variable dni busca conincidir con el dni del indice en el diccionario
    dni=int(input("ingrese el dni del empleado:"))
    if dni in busqueda:
        print(dni, busqueda[dni][0])
        for materias in busqueda[dni][1]:
            print(materias[0],materias[1])

#------------------------bloque principal---------------------------------------------

lista=carga()

listado(lista)

consulta(lista)

