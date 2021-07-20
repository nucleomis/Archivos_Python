from admin_archivos import devolver_nombre
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

#---------------------informes:-------------------------------------


#lsita de usuarios registrados:
def lista_usuarios():
    lis = []
    archivo = open("jugador.txt","r")
    linea = archivo.readline()
    while linea !="":
        lista = linea.split(",")
        linea = archivo.readline()
        lis.append([lista[0],borrar_salto(lista[1])])
    archivo.close()
    print("LISTA DE JUGADORES:\n")
    print("          | ID |NOMBRE    |")
    print("          ________________")
    for x in range(len(lis)):
        print(f"          |{cont_con_long(4,lis[x][0])}|{cont_con_long(10,lis[x][1])}|")
        print("          ________________")
    op = input("presiones ENTER para volver al menu")
    consola()

#informe de puntajes de jugador:
def puntaje_jugador(nombre,id_jugador):
    matriz =[]
    long = os.path.getsize("partida.txt")
    cant_lineas = long//74#me dice cuantas lineas tiene el archivo
    archivo = open("partida.txt", "r")
    pos = 0
    cont = True
    while cont:
        pos +=1
        archivo.seek(long-(74*pos))
        linea = archivo.readline()
        lista = linea.split(",")
        cant_lineas = cant_lineas-1
        if borrar_car_exedente(lista[1])==id_jugador:
            matriz.append(lista)
            reg_anterior = int(borrar_car_exedente(lista[7]))
            continuar = borrar_car_exedente(lista[8])
            while int(continuar) >0:
                puntero = 74*(reg_anterior-1)
                archivo.seek(puntero)
                linea= archivo.readline()
                lista = linea.split(",")
                matriz.append(lista)
                reg_anterior = int(borrar_car_exedente(lista[7]))
                continuar = borrar_salto(borrar_car_exedente(lista[8]))
                if continuar == "0":
                    cont = False
            archivo.close()
    limpiar()
    print(f"Nombre: {nombre}       ID:{borrar_car_exedente(matriz[0][1])}")
    print("___________________________________________________________________________")
    print("nº partida|col raqueta1|col raqueta2|total col|         fecha      |Puntos|")
    print("___________________________________________________________________________")
    for x in range(len(matriz)):
        print(f"|    {cont_con_long(5,borrar_car_exedente(matriz[x][0]))}|      {cont_con_long(6,borrar_car_exedente(matriz[x][4]))}|      {cont_con_long(6,borrar_car_exedente(matriz[x][5]))}|   {cont_con_long(6,borrar_car_exedente(matriz[x][6]))}|  {cont_con_long(18,borrar_car_exedente(matriz[x][2]))}|   {cont_con_long(3,borrar_car_exedente(matriz[x][3]))}|")
        print("___________________________________________________________________________")
    puntos = records(matriz)
    print(f"*Mejor partida: {borrar_car_exedente(puntos[0])}   *Peor partida: {borrar_car_exedente(puntos[1])}")
    op = input("presiones ENTER para volver al menu")
    consola()

def informe_colisiones( num_partida, id_jugador):
    archivo = open("colisiones.txt", "r")
    linea = archivo.readline()
    matriz = []
    while linea !="":
        lista = linea.split(",")
        if str(num_partida) == borrar_car_exedente(lista[0]) and str(id_jugador)==borrar_car_exedente(lista[1]):
            while str(num_partida) == borrar_car_exedente(lista[0]):
                lista = linea.split(",")
                matriz.append(lista)
                linea = archivo.readline()
            archivo.close()
        else: 
            linea = archivo.readline()
    archivo.close()
    limpiar()
    print("Informe de colisiones por partida: ")
    print("___________________________________")
    print(f"**usuario: {borrar_salto(dev_nom_x_id(id_jugador)).upper()}  ** num de partida: {num_partida}")
    print("--------------------------------------------------------------")
    print("fecha     |hora    | eje x/ eje y|   observacion  |")
    print("_________________________________________________")
    for x in range(len(matriz)-1):
        print(f"|{borrar_car_exedente( matriz[x][2])}|   {cont_con_long(10, borrar_car_exedente( matriz[x][3]))}| {borrar_salto(borrar_car_exedente(matriz[x][4]))}|")
        print("--------------------------------------------------")
    o = input("presione ENTER para volver al menu")
    consola()

def informe_total_colisiones_partida(num_partida,nombre_jugador):
    archivo = open("partida.txt","r")
    puntero = 74*(int(num_partida)-1)
    archivo.seek(puntero)
    linea = archivo.readline()
    lista = linea.split(",")
    print("*PUNTAJE POR COORENADAS: \n")
    print(f"*Numero de partida: {num_partida}\nnombrejugador: {nombre_jugador}")
    print("______________________________________")
    print("Objeto pala|    pelota   | Total Pje |")
    print("______________________________________")
    print(f"    1      |      {cont_con_long(6, borrar_car_exedente(lista[4]))} |     {cont_con_long(6,borrar_car_exedente(lista[4]))}|")
    print("______________________________________")
    print(f"    2      |      {cont_con_long(6,cont_con_long(6, borrar_car_exedente(lista[5])))} |     {cont_con_long(6,borrar_car_exedente(lista[5]))}|")
    print("______________________________________")
    op = input("presiones ENTER para volver al menu")
    consola()

def rank_partidas():
    archivo = open("partida.txt","r")
    lista = archivo.readline()
    matriz = []
    while lista !="":
        linea = lista.split(",")
        matriz.append(linea)
        lista = archivo.readline()
    ordenado = lista_records(matriz)
    archivo.close()
    limpiar()
    print("RANKING DE PARTIDAS: ")
    print("______________________________________________________________\n")
    print("cod usuario|     nombre    | total paleta 1| total paleta 2| Puntos| total colisiones")
    print("--------------------------------------------------------------------------------------")
    for x in range(len(ordenado)):
        print(f"     {cont_con_long(6, borrar_car_exedente(ordenado[x][1]))}|     {cont_con_long(10,borrar_salto(dev_nom_x_id(borrar_car_exedente(ordenado[x][1]))))}|       {cont_con_long(8, borrar_car_exedente(ordenado[x][4]))}|       {cont_con_long(8, borrar_car_exedente(ordenado[x][5]))}|   {cont_con_long(4, borrar_car_exedente(ordenado[x][3]))}|    {cont_con_long(8, borrar_car_exedente(ordenado[x][6]))}|")

    print("______________________________________________________________________________________")
    print(f"**mejor jugador: {borrar_car_exedente(ordenado[0][3])}  **peor jugador: {borrar_car_exedente(ordenado[-1][3])}")
    op = input("presiones ENTER para volver al menu")
    consola()
            

def informe_anual(nombre_jugador,año):
    #creo la matriz para crear el informe anual
    dias=[]#matriz a modificar con los datos segun el dia ,el mes y el año
    sub_total=[]
    for x in range (30):#creo la matriz donde voy a cargar las fechas
        meses=[]
        sub=0
        sub_total.append(sub)
        for k in range (12):
            meses.append("|"+cont_con_long(4,""))
        dias.append(meses)
    matriz =[]
    long = os.path.getsize("partida.txt")
    archivo = open("partida.txt", "r")
    pos = 0
    cont = True
    while cont ==True:
        pos +=1 
        archivo.seek(long-74*pos)
        linea = archivo.readline()
        lista = linea.split(",")
        ref_id = devolver_id_jugador(nombre_jugador)
        if borrar_car_exedente(lista[1]) == ref_id:
            matriz.append(lista)
            reg_anterior = int(borrar_car_exedente(lista[7]))
            continuar = borrar_car_exedente(lista[8])
            while int(continuar) >0:
                puntero = 74*(reg_anterior-1)
                archivo.seek(puntero)
                linea= archivo.readline()
                lista = linea.split(",")
                matriz.append(lista)
                reg_anterior = int(borrar_car_exedente(lista[7]))
                continuar = borrar_salto(borrar_car_exedente(lista[8]))
                if continuar == "0":
                    archivo.seek(puntero)
                    linea= archivo.readline()
                    lista = linea.split(",")
                    matriz.append(lista)
                    cont = False
            archivo.close()

    fecha = []
    M_por_año = []
    for x in range (len(matriz)):#creo una matriz con la fecha de cada registro
        #para usarla de manera paralela
        f = borrar_car_exedente(matriz[x][2])
        date = f.split("/")
        fecha.append([date[0],date[1],date[2][0:4]])
        #voy a generar la matriz solo con los elementos que conincidan en el año
        if str(fecha[x][2]) == str(año):
            M_por_año.append([fecha[x][0],fecha[x][1], borrar_car_exedente(matriz[x][6])])

    #sumo los puntos de los eventos el mismo dia:
    acum = int(M_por_año[0][2])
    for x in range (len(M_por_año)-1):
        sub_total[(int(M_por_año[x][0]))-1] += int(M_por_año[x][2])
            
        if M_por_año[x][0]==M_por_año[x+1][0]:
            acum += int(M_por_año[x+1][2])
        else:
            dias[(int(M_por_año[x][0]))-1][(int(M_por_año[x][1]))-1]="|"+cont_con_long(4,str(acum))
            acum = int(M_por_año[x+1][2])
        if x==(len(M_por_año))-2:
            acum = acum-int(M_por_año[-1][2])
    dias[(int(M_por_año[-1][0]))-1][(int(M_por_año[-1][1]))-1]="|"+cont_con_long(4,str(acum))
    
    #saco el total de todos los impactos
    total  = 0
    for x in range(len(sub_total)):
        total += sub_total[x]

    limpiar()        
    cont = 0
    print(f"NOMBRE: {nombre_jugador}                 AÑO: {año}")
    print("*MESES:        1        2        3        4        5        6        7        8        9       10       11       12 | sub_total")
    print("----------------------------------------------------------------------------------------------------------------------")
    print("*Dias:     |        |        |        |        |        |        |        |        |        |        |        |     |  ")
    print("----------------------------------------------------------------------------------------------------------------------")
    for x in range(len(dias)):
        cont +=1
        print(f"     {cont_con_long(4,str(cont))}{dias[x]}|  {cont_con_long(5,str(sub_total[x]))}")

    print("----------------------------------------------------------------------------------------------------------------------------------")        
    print("                                           TOTAL: ",total) 
    op = input("presiones ENTER para volver al menu")
    consola()      
    

def informe_anual_objetos(nombre_jugador,año):
    #creo la matriz para crear el informe anual
    dias=[]#matriz a modificar con los datos segun el dia ,el mes y el año
    sub_total=[]
    for x in range (3):#creo la matriz donde voy a cargar las fechas
        meses=[]
        sub=0
        sub_total.append(sub)
        for k in range (12):
            meses.append("|"+cont_con_long(4,""))
        dias.append(meses)
    matriz =[]
    long = os.path.getsize("partida.txt")
    archivo = open("partida.txt", "r")
    pos = 0
    cont = True
    while cont ==True:
        pos +=1 
        archivo.seek(long-74*pos)
        linea = archivo.readline()
        lista = linea.split(",")
        ref_id = devolver_id_jugador(nombre_jugador)
        if borrar_car_exedente(lista[1]) == ref_id:
            matriz.append(lista)
            reg_anterior = int(borrar_car_exedente(lista[7]))
            continuar = borrar_car_exedente(lista[8])
            while int(continuar) >0:
                puntero = 74*(reg_anterior-1)
                archivo.seek(puntero)
                linea= archivo.readline()
                lista = linea.split(",")
                matriz.append(lista)
                reg_anterior = int(borrar_car_exedente(lista[7]))
                continuar = borrar_salto(borrar_car_exedente(lista[8]))
                if continuar == "0":
                    archivo.seek(puntero)
                    linea= archivo.readline()
                    lista = linea.split(",")
                    matriz.append(lista)
                    cont = False
            archivo.close()

    fecha = []
    M_por_año = []
    for x in range (len(matriz)):#creo una matriz con la fecha de cada registro
        #para usarla de manera paralela
        f = borrar_car_exedente(matriz[x][2])
        date = f.split("/")
        fecha.append([date[0],date[1],date[2][0:4]])
        #voy a generar la matriz solo con los elementos que conincidan en el año
        if str(fecha[x][2]) == str(año):
            M_por_año.append([fecha[x][0],fecha[x][1], borrar_car_exedente(matriz[x][6])])

    #sumo los puntos de los eventos el mismo dia:
    acum = int(M_por_año[0][2])
    for x in range (len(M_por_año)-1):
        sub_total[(int(M_por_año[x][0]))-1] += int(M_por_año[x][2])
            
        if M_por_año[x][0]==M_por_año[x+1][0]:
            acum += int(M_por_año[x+1][2])
        else:
            dias[(int(M_por_año[x][0]))-1][(int(M_por_año[x][1]))-1]="|"+cont_con_long(4,str(acum))
            acum = int(M_por_año[x+1][2])
        if x==(len(M_por_año))-2:
            acum = acum-int(M_por_año[-1][2])
    dias[(int(M_por_año[-1][0]))-1][(int(M_por_año[-1][1]))-1]="|"+cont_con_long(4,str(acum))
    
    #saco el total de todos los impactos
    total  = 0
    for x in range(len(sub_total)):
        total += sub_total[x]

    limpiar()        
    cont = 0
    print(f"NOMBRE: {nombre_jugador}                 AÑO: {año}")
    print("*MESES:        1        2        3        4        5        6        7        8        9       10       11       12 | sub_total")
    print("----------------------------------------------------------------------------------------------------------------------")
    print("*Dias:     |        |        |        |        |        |        |        |        |        |        |        |     |  ")
    print("----------------------------------------------------------------------------------------------------------------------")
    for x in range(len(dias)):
        cont +=1
        print(f"     {cont_con_long(4,str(cont))}{dias[x]}|  {cont_con_long(5,str(sub_total[x]))}")

    print("----------------------------------------------------------------------------------------------------------------------------------")        
    print("                                           TOTAL: ",total) 
    op = input("presiones ENTER para volver al menu")
    consola()      




               

    
#----------------consola-------------------------------

def consola():
    limpiar()
    try:
        print("\nSeleccione el numero informe:\n")
        print("1) lista de jugadores")
        print("2) ranking de partidas por jugador")
        print("3) consulta por usuario y numero de partida")
        print("4) consulta ranking de partidas")
        print("5) informe de colisiones")
        print("6) informe de  anual de interaccion de los objetos")

        op = int(input("\nopcion: "))
    
        if op ==1:#padron usuarios del jeugo
            limpiar()
            lista_usuarios()
        else:
            if op==2:#consulta por jugador
                limpiar()
                nombre = input("ingrese el nombre del jugador: ")
                verif = verificar_nom_jugador(nombre)
                print(nombre)
                if verif == True:
                    limpiar()
                    id = devolver_id_jugador(nombre)
                    puntaje_jugador(nombre,id)
                else:
                    print("EL JUGADOR NO EXISTE")
                    o = input("presione ENTER para regresar")
                    consola()
            else:
                if op == 3:#usuario y numero de partida
                    limpiar()
                    nom = input("Ingrese el nombre del jugador: ")
                    part = int(input("ingrese el numero de partida: "))
                    ver = verificar_partida(nom, str(part))
                    id = devolver_id_jugador(nom)
                    if ver:
                        informe_total_colisiones_partida(id,nom)
                else: 
                    if op ==4:
                        rank_partidas()
                    else:
                        if op ==5:
                            limpiar()
                            nombre = input("ingrese el nombre del jugador: ")
                            partida = input("ingrese el numero de partida: ")
                            verpart = verificar_partida(str(nombre),str(partida))
                            if verpart == True:
                                id = devolver_id_jugador(nombre)
                                informe_colisiones(partida, id)
                            else:
                                print("el jugador no existe")
                                o = input("presione ENETER para volver al menu")
                                consola()
                        else:
                            if op == 6:
                                limpiar()
                                n = input("ingrese el nombre del jugador: ")
                                año = input("ingrese el año solicitado: ")
                                informe_anual(n,año)
                            else: 
                                if op <1 or op>6:
                                    limpiar()
                                    print("ERROR opcion no valida")
                                    o = input("presione ENTER para volver al menu")
                                    consola()
    except:
        limpiar()
        print("ERROR PRESTA ATENCION")
        o = input("presione ENTER para volver al menu")
        consola()

#-------------------ejecucion-------------------------

consola()

