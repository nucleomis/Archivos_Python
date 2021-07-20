from datetime import datetime
import os

hoy = datetime.now()
dia = (f"{hoy.date().day}/{hoy.date().month}/{hoy.date().year} H {hoy.now().hour}:{hoy.now().minute}")
dias = (f"{hoy.date().day}/{hoy.date().month}/{hoy.date().year}")
#------------------FUNCIONES PARA PROCESAR LOS DATOS PARA LOS ARCHIVOS------------------

def borrar_car_exedente(contenido):
    for char in "_":
        contenido=contenido.replace(char,"")
    return str(contenido)

def borrar_salto(contenido):
    for char in "\n":
        contenido=contenido.replace(char,"")
    return str(contenido)

#funcion para determinar el largo del contenido y completar con "_" los espacios restantes
def cont_con_long(longitud_del_segmento,contenido):
    lista=contenido+("_"*(longitud_del_segmento-len(contenido)))
    return lista

#----------------FUNCIONES DE VERIFICACION--------------------------------------------------

#funcion que devuelve el nombre pasandole el id de jugador:
def dev_nom_x_id(id_jugador):
    archivo = open("jugador.txt","r")
    linea = archivo.readline()
    lista = linea.split(",")
    while linea !="":
        if lista[0] == str(id_jugador):
            return lista[1]
        linea = archivo.readline()
        lista = linea.split(",")
    archivo.close()

#funcion que verifica si existe el jugador
def verificar_jugador(nombre):
    archivo=open("jugador.txt","r")
    lineas = archivo.readline()
    while lineas!="":
        lista=lineas.split(",")
        lineas = archivo.readline()
        dato=lista[1]
        dato= dato[0:len(dato)-1]
        if nombre==dato:
            return True
    archivo.close()
    return False

#funcion que devuelve el nombre del jugador

def devolver_nombre(nombre):
    archivo=open("jugador.txt","r")
    lineas = archivo.readline()
    while lineas!="":
        lista=lineas.split(",")
        lineas = archivo.readline()
        dato=lista[1]
        dato= dato[0:len(dato)-1]
        if nombre==dato:
            return dato.upper()
    archivo.close()
    return False

def devolver_id_jugador(nombre):
    archivo=open("jugador.txt","r")
    lineas = archivo.readline()
    while lineas!="":
        lista=lineas.split(",")
        lineas = archivo.readline()
        dato=lista[1]
        dato= dato[0:len(dato)-1]
        if nombre==dato:
            return lista[0]
    archivo.close()

#------------------ FUNCION DE CARGA DE DATOS -------------------------------------------

#funcion que devuelve el ultimo registro para el enlace
def num_ultimo_reg(id_jugador):
    long = os.path.getsize("partida.txt")
    cant_lineas = long//74#me dice cuantas lineas tiene el archivo
    archivo = open("partida.txt", "r")
    pos = 0
    while cant_lineas>0:
        pos +=1
        archivo.seek(long-(74*pos))
        linea = archivo.readline()
        lista = linea.split(",")
        cant_lineas = cant_lineas-1
        if str(id_jugador)==borrar_car_exedente(lista[1]):
            archivo.close()
            cant_lineas = 1
            return borrar_car_exedente(lista[0]),str(1)
        else:
            if cant_lineas ==0 and str(id_jugador) !=borrar_car_exedente(lista[1]):
                archivo.close()
                return str(0), str(0)

#funcion para cargar colisiones entre pelota roja y verde:
def colision_entre_objetos(usuario,rect_x,rect_y, pala,pelota,color):
    num_partida =cont_con_long(5 , str((os.path.getsize("partida.txt") //74)+1))
    fecha = dias
    archivo = open("colipelo.dat", "a+")
    archivo.write(f"{usuario},{fecha},{num_partida},{rect_x},{rect_y},{pala},{pelota},{color}\n")
    archivo.close()

#colisiones entre pelota roja y verde
def colision_verde_rojo(nom_usuario,rect_x,rect_y):
    cod = devolver_id_jugador(nom_usuario)
    num_partida =cont_con_long(5 , str((os.path.getsize("partida.txt") //74)+1))
    fecha = dias
    archivo = open("colirove.dat","a+")
    archivo.write(f"{cod},{dias},{num_partida},pelota_roja,pelota_verde,{rect_x},{rect_y}\n")
    archivo.close()


#funcion para cargar el nombre del jugador
def cargar_jugador(nombre):
    archivo = open("jugador.txt", "r")
    cont = 0
    linea = archivo.readline()
    while linea !="":
        cont +=1
        linea = archivo.readline()
    cont +=1
    archivo.close()
    #----------------------------------
    archivo = open("jugador.txt","a")
    archivo.write(str(cont))
    archivo.write(",")
    archivo.write(str(nombre))
    archivo.write("\n")
    archivo.close()


#funcion para cargar la partida del jugador
#este historial tiene que contener:
#id del jugador, id partida,puntaje, golpes 
def carga_historial_por_partida(nombre, total_puntos,total_raqueta1,total_raqueta2,total_impactos):
    num_partida =cont_con_long(5 , str((os.path.getsize("partida.txt") //74)+1))
    archivo = open("partida.txt", "a")
    id = cont_con_long(9,devolver_id_jugador(nombre))
    fecha = cont_con_long(18,str(dia))
    raqueta1 = cont_con_long(4, str(total_raqueta1))
    raqueta2 = cont_con_long(4,str(total_raqueta2))
    puntos = cont_con_long(7,str(total_puntos))
    impactos = cont_con_long(7,str(total_impactos))
    enlace = num_ultimo_reg(borrar_car_exedente(id))
    archivo.write(str(num_partida))
    archivo.write(",")
    archivo.write(id)
    archivo.write(",")
    archivo.write(str(fecha))
    archivo.write(",")
    archivo.write(str(puntos))
    archivo.write(",")
    archivo.write(str(raqueta1))
    archivo.write(",")
    archivo.write(str(raqueta2))
    archivo.write(",")
    archivo.write(str(impactos))
    archivo.write(",")
    archivo.write(cont_con_long(5,str(enlace[0])))
    archivo.write(",")
    archivo.write(cont_con_long(5,str(enlace[1])))
    archivo.write("\n")


#funcion que graba cada colision
def archivo_colisiones(nombre,coordenada, observacion):
    num_partida = cont_con_long(5 , str((os.path.getsize("partida.txt") //74)+1))
    archivo = open("colisiones.txt","a")
    usuario = devolver_id_jugador(str(nombre))
    fecha = dia
    archivo.write(cont_con_long(4,str(num_partida)))
    archivo.write(",")
    archivo.write(cont_con_long(4,str(usuario)))
    archivo.write(",")
    archivo.write(cont_con_long(18,fecha))
    archivo.write(",")
    archivo.write(cont_con_long(8,str(coordenada)))
    archivo.write(",")
    archivo.write(cont_con_long(15,str(observacion)))
    archivo.write("\n")

    




def records():
    lon = os.path.getsize("partida.txt")
    vueltas = lon //72
    matriz = []
    archivo = open("partida.txt","r")
    linea = archivo.readline()
    lista = linea.split(",")
    datos = borrar_salto(dev_nom_x_id(borrar_car_exedente(str(lista[1])))),borrar_car_exedente(lista[3]),borrar_car_exedente(lista[2])
    matriz.append(datos)
    while vueltas>1:
        linea = archivo.readline()
        lista = linea.split(",")
        datos = borrar_salto(dev_nom_x_id(borrar_car_exedente(str(lista[1])))),borrar_car_exedente(lista[3]),borrar_car_exedente(lista[2])
        matriz.append(datos)
        vueltas = vueltas - 1
    archivo.close()
    lon = len(matriz)-1
    for k in range (lon):
        for x in range (lon-k):
            if int(matriz[x][1])<int(matriz[x+1][1]):
                aux = matriz[x]
                matriz[x]= matriz[x+1]
                matriz[x+1]= aux
    top =[]
    for x in range (10):
        top.append(matriz[x])
    return top

archivo = open("jugador.txt","r")
linea= archivo.readline()
