from admin_archivos import archivo_colisiones
import os

def limpiar():
    os.system("cls")
    print("---------consola de informes:--------\n")


def borrar_salto(contenido):
    for char in "\n":
        contenido=contenido.replace(char,"")
    return str(contenido)

def cont_con_long(longitud_del_segmento,contenido):
    lista=contenido+(" "*(longitud_del_segmento-len(contenido)))
    return lista

def borrar_car_exedente(contenido):
    for char in "_":
        contenido=contenido.replace(char,"")
    return str(contenido)

def dev_nom_x_id(id_jugador):
    archivo = open("jugador.txt","r")
    linea = archivo.readline()
    lista = linea.split(",")
    while linea !="":
        if lista[0] == str(id_jugador):
            return borrar_car_exedente (lista[1])
        linea = archivo.readline()
        lista = linea.split(",")
    archivo.close()

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

def verificar_nom_jugador(nombre):
    archivo = open("jugador.txt","r")
    linea = archivo.readline()
    while linea !="":
        lista = linea.split(",")
        if str(nombre) == borrar_salto(lista[1]):
            archivo.close()
            return True
        linea = archivo.readline()
    archivo.close()
    return False

def records(matriz):
    lon = len(matriz)-1
    for k in range (lon):
        for x in range (lon-k):
            if int(borrar_car_exedente(matriz[x][3]))<int(borrar_car_exedente(matriz[x+1][3])):
                aux = (matriz[x])
                matriz[x]= matriz[x+1]
                matriz[x+1]= aux
    return matriz[0][3], matriz[-1][3]

def lista_records(matriz):
    lon = len(matriz)-1
    for k in range (lon):
        for x in range (lon-k):
            if int(borrar_car_exedente(matriz[x][3]))<int(borrar_car_exedente(matriz[x+1][3])):
                aux = (matriz[x])
                matriz[x]= matriz[x+1]
                matriz[x+1]= aux
    return matriz

def verificar_partida(nombre_usuario, numero_partida):
    archivo = open("partida.txt","r")
    linea = archivo.readline()
    id = devolver_id_jugador(nombre_usuario)
    while linea !="":
        lista = linea.split(",")
        partida = borrar_car_exedente(lista[0])
        nom = borrar_car_exedente(lista[1])
        if partida == numero_partida and nom == id:
            return True
        linea = archivo.readline()
    archivo.close()
    return False





def informe_anual_objetos(nombre_jugador,año_a_buscar):
    #creo la matriz para crear el informe
    lineas=[]#matriz a modificar con los datos segun el dia ,el mes y el año
    sub_total=[]#creo la matriz para los subtotales

    for x in range (3):#creo la matriz donde voy a cargar las fechas, filas
        meses=[]
        sub_total.append(0)
        for k in range (12): # columnas
            meses.append(0)
        lineas.append(meses)

    #separo la fecha en otra lista donde la coincida el año
    jugador =[]
    meses_juego = []
    archivo= open("colipelo.dat","r")
    lista = archivo.readline()
    while lista !="":
        linea = lista.split(",")
        fecha = linea[1].split("/")
        año = fecha[2]
        mes = fecha[1]
        if linea[0] == nombre_jugador and año == año_a_buscar:
            meses_juego.append(mes)
            jugador.append(linea)
            
        lista = archivo.readline()
    archivo.close()

    #tomo la lista con el valor de la posicion de la matriz que quiero modificar
    #es este caso uso la matriz meses como valor y el color como referencia
    total_impactos = 0
    for x in range(len(meses_juego)):
        color = borrar_salto(jugador[x][7])
        if color == "roja":
            lineas[0][int(meses_juego[x])-1] += 1
            sub_total[0] +=1
            total_impactos +=1
        if color == "azul":
            lineas[1] [int(meses_juego[x])-1] +=1
            sub_total[1] +=1
            total_impactos +=1
        if color == "verde":
            lineas[2] [int(meses_juego[x])-1] +=1
            sub_total[2] +=1
            total_impactos +=1
            
    #preparo la matriz para imprimir, convierto en string con longitud
    for x in range (len(lineas)):
        for k in range (len(lineas[x])):
            lineas[x][k] = f"  {cont_con_long(2,str(lineas[x][k]))} "

    limpiar()
    cont = 0
    print(f"NOMBRE: {nombre_jugador}                 AÑO: {año_a_buscar}")
    print("*meses:        1        2        3        4        5        6        7        8        9       10       11       12 | sub_total")
    print("----------------------------------------------------------------------------------------------------------------------")
    print("*objetos:  |        |        |        |        |        |        |        |        |        |        |        |     |  , ")
    print("----------------------------------------------------------------------------------------------------------------------")
    for x in range(len(lineas)):
        cont +=1
        print(f"    {cont_con_long(4,str(cont))}   {lineas[x]}|  {cont_con_long(2,str(sub_total[x]))}")

    print("----------------------------------------------------------------------------------------------------------------------------------")        
    print("                                           TOTAL: ",total_impactos) 
    op = input("presiones ENTER para volver al menu")
        

#informe_anual_objetos("fa","2020")