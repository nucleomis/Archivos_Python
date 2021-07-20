# Importacioness e inicializaciones
import pygame, pruebas
import sys,os,admin_archivos,menu

from pygame import rect
from admin_archivos import archivo_colisiones,colision_entre_objetos,colision_verde_rojo
from read_data import Jugador as nom


def limpiar():
    os.system("cls")

pygame.init()

# configuracion de ventana principal

ventana = pygame.display.set_mode((750, 500))

pygame.display.set_caption('tp programacion')

# Colores

blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0,255,0)
azul = (0, 0, 255)
#---------------------------------------------------------------------------------------

#                                         Clases

class Raqueta1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 75])
        self.image.fill(verde)
        self.rect = self.image.get_rect()
        self.puntos = 0
        self.velocidad = 0


class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([18, 18])
        self.rect = (self.image.get_rect())
        #dibujo un circulo dentro del contenedor de imagen
        self.velocidad = 0
        self.dx = 1
        self.dy = 1

    def colores(self,color):
        self.color = color
        self.circulo = pygame.draw.circle(self.image,self.color,(9,9),8,0)

    def rebotar(self):
        if self.rect.y > 490:
            self.dy = -1
    
        if self.rect.y < 1:
            self.dy = 1

        if self.rect.x > 740:
            self.rect.x, self.rect.y = 375, 250
            self.dx = -1
            
        if self.rect.x < 1:
            self.rect.x, self.rect.y = 375, 250
            self.dx = 1
            



class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("nave.png").convert()
        self.image.set_colorkey(blanco)
        self.rect = self.image.get_rect()
        self.velocidad_x = 0
        self.vidas = 6
        self.cadencia = 100
        self.disparo_anterior = pygame.time.get_ticks()



class Disparo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([3, 20])
        self.image.fill(verde)
        self.rect = self.image.get_rect()
        self.puntos = 0
        self.velocidad = 0
    def update(self):
        self.rect.y -= 10

#------------------------------------------------------------------------------------------------
#                          creacion de las variables para los sprites

col = 0

raqueta1 = Raqueta1()
raqueta1.rect.x = 10
raqueta1.rect.y = 225
raqueta1.puntos = 10

raqueta2 = Raqueta1()
raqueta2.rect.x = 730
raqueta2.rect.y = 225
raqueta2.puntos = 0


raqueta_velocidad = 20

pelota = Pelota()
pelota.rect.x = 375
pelota.rect.y = 250
pelota.colores(azul)

pelota_roja = Pelota()
pelota_roja.rect.x = 375
pelota_roja.rect.y = 250
pelota_roja.colores(rojo)

pelota_verde = Pelota()
pelota_verde.rect.x = 375
pelota_verde.rect.y = 250
pelota_verde.colores(verde)





#--------------------------------------------------------------------------------------------------
#                             funcion de escritura de la pantalla

def juego(nombre_j,todo_sprites):
   
    # pone la pantalla en negro
    ventana.fill(negro)
    pygame.draw.circle(ventana, blanco, (375,250), 150, 1)
    pygame.draw.line(ventana, blanco, (375,1),(375,500), 1)

    # Fuente del titulo
    font = pygame.font.SysFont('Comic Sans MS', 30)
    text = font.render('TP: Pin Pong', False, blanco)
    textRect = text.get_rect()
    textRect.center = (750 // 2, 25)
    ventana.blit(text, textRect)

    # vidas del player 1
    p1_punto = font.render("VIDAS: ", False, azul)
    p1_punto_rect= p1_punto.get_rect()
    p1_punto_rect.center = (60,20)
    ventana.blit(p1_punto,p1_punto_rect)
    p1_score = font.render(str(raqueta1.puntos), False, blanco)
    p1Rect = p1_score.get_rect()
    p1Rect.center = (90, 50)
    ventana.blit(p1_score, p1Rect)
    
    # puntaje del player 2
    p2_punto = font.render("puntos: ", False, azul)
    p2_punto_rect= p1_punto.get_rect()
    p2_punto_rect.center = (680,20)
    ventana.blit(p2_punto,p2_punto_rect)
    p2_score = font.render(str(raqueta2.puntos), False, blanco)
    p2Rect = p2_score.get_rect()
    p2Rect.center = (700, 50)
    ventana.blit(p2_score, p2Rect)

    font = pygame.font.SysFont('Comic Sans MS', 30)
    textnom = font.render(nombre_j, False, blanco)
    textnomRect = textnom.get_rect()
    textnomRect.center = (750 // 2, 55)
    ventana.blit(textnom, textnomRect)
    
    # actualizacion de todos los sprites
    todo_sprites.draw(ventana)
    # Actualizacion de escritura de pantalla
    pygame.display.update()

#----------------------------------------------------------------------------

# bucle principal

def main(correrOno,nombre):
     # Groupo de Sprites
    grupo_laser = pygame.sprite.Group()
    todo_sprites = pygame.sprite.Group()
    todo_sprites.add(raqueta1, raqueta2, pelota,pelota_verde,pelota_roja)
    colision_raqueta1= col
    colision_raqueta2= col
    colisiones = col
    raqueta2.velocidad = 10
    pelota.velocidad = 11
    pelota_verde.velocidad = 9
    pelota_roja.velocidad = 5
    pelotava = False
    contador = 0
    while correrOno:
        contador += 1
        pygame.time.delay(100)
    # control de quitar
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
            

    # movimiento de las raquetas
    #---------------------------
    #defino a tecla como la funcion para obtener la tecla precionada
        tecla = pygame.key.get_pressed()
        
    #raqueta1:
        if tecla[pygame.K_w]:
            raqueta1.rect.y += -raqueta_velocidad
        if tecla[pygame.K_s]:
            raqueta1.rect.y += raqueta_velocidad
    #--------------------------------------------
    #raqueta 2: 
        if contador==200:
            raqueta1.rect.y += -(raqueta2.velocidad+2)
            raqueta1.rect.y += raqueta2.velocidad+2

        if tecla[pygame.K_UP]:#arriba
            raqueta2.rect.y += int(-raqueta2.velocidad)
        if tecla[pygame.K_DOWN]:#abajo
            raqueta2.rect.y += int(raqueta2.velocidad)

    #--------------------------------------------
    #ia raqueta 2:
        if pelotava == True and raqueta2.rect.y>=220:#busca volver al medio
            raqueta2.rect.y += int(-raqueta2.velocidad)
    
        if pelotava == True and raqueta2.rect.y<=220:#busca volver al medio
            raqueta2.rect.y += int(raqueta2.velocidad)

        else:
            if pelotava == False and (pelota.rect.y)-16 <= raqueta2.rect.y:
                if pelota.rect.x>=275:
                    if raqueta2.rect.y >= 10:
                        raqueta2.rect.y += -int(raqueta2.velocidad)
            else:
                if (pelota.rect.y)+12 >= raqueta2.rect.y and pelota.rect.x>=275:
                    if raqueta2.rect.y <= 420:            
                        raqueta2.rect.y += int(raqueta2.velocidad)
    

    # movimiento de la pelota
        pelota.rect.x += pelota.velocidad * pelota.dx+1
        pelota.rect.y += pelota.velocidad * pelota.dy+1

        #pelota roja
        pelota_roja.rect.x += pelota_roja.velocidad *pelota_roja.dx+1
        pelota_roja.rect.y += pelota_roja.velocidad * pelota_roja.dy+1

        #pelota verde
        pelota_verde.rect.x += pelota_verde.velocidad *pelota_verde.dx+1
        pelota_verde.rect.y += pelota_verde.velocidad * pelota_verde.dy+1

    # rebote entre pared y paletas con la pelota/s
        pelota.rebotar()
        if pelota.rect.x > 738:
            raqueta2.puntos += 1

        if pelota.rect.x < 1:
            raqueta1.puntos += -1
            pelotava = False

        #pelota roja
        pelota_roja.rebotar()
        if pelota_roja.rect.x > 738:
            raqueta2.puntos += 1

        if pelota_roja.rect.x < 1:
            raqueta1.puntos += -1
            pelotava = False

        #pelota verde
        pelota_verde.rebotar()
        if pelota_verde.rect.x > 738:
            raqueta2.puntos += 1

        if pelota_verde.rect.x < 1:
            raqueta1.puntos += -1
            pelotava = False    

    #colision con las raquetas

        #pelota azul
        if raqueta1.rect.colliderect(pelota.rect):
            pelota.dx = 1
            pelotava = False
            colisiones += 1
            colision_raqueta1 = colision_raqueta1 + 1
            archivo_colisiones(str(nombre),(f"{raqueta1.rect.x}/{raqueta1.rect.y}"),"raqueta1/pelota")
            colision_entre_objetos(str(nombre),str(raqueta1.rect.x),str(raqueta1.rect.y),"raqueta1","pelota","azul")
        #raqueta 1 pelota roja
        if raqueta1.rect.colliderect(pelota_roja.rect):
            pelota_roja.dx = 1
            pelotava = False
            colisiones += 1
            colision_raqueta1 = colision_raqueta1 + 1
            raqueta1.puntos += 1
            archivo_colisiones(str(nombre),(f"{raqueta1.rect.x}/{raqueta1.rect.y}"),"raqueta1/pelota_roja")
            colision_entre_objetos(str(nombre),str(raqueta1.rect.x),str(raqueta1.rect.y),"raqueta1","pelota","roja")
            
        # raqueta 1 pelota verde
        if raqueta1.rect.colliderect(pelota_verde.rect):
            pelota_verde.dx = 1
            pelotava = False
            colisiones += 1
            colision_raqueta1 = colision_raqueta1 + 1
            raqueta1.puntos += 1
            archivo_colisiones(str(nombre),(f"{raqueta1.rect.x}/{raqueta1.rect.y}"),"raqueta1/pelota_verde")
            colision_entre_objetos(str(nombre),str(raqueta1.rect.x),str(raqueta1.rect.y),"raqueta1","pelota","verde")

        #colisiones raqueta2 
        if raqueta2.rect.colliderect(pelota.rect):
            pelotava= True
            pelota.dx = -1
            colisiones += 1
            colision_raqueta2 += 1
            archivo_colisiones(str(nombre),(f"{raqueta2.rect.x}/{raqueta2.rect.y}"),"raqueta2/pelota")
            colision_entre_objetos(str(nombre),str(raqueta1.rect.x),str(raqueta1.rect.y),"raqueta2","pelota","azul")

            #colision pelota verde
        if raqueta2.rect.colliderect(pelota_verde.rect):
            pelotava= True
            pelota_verde.dx = -1
            colisiones += 1
            colision_raqueta2 += 1
            
            archivo_colisiones(str(nombre),(f"{raqueta2.rect.x}/{raqueta2.rect.y}"),"raqueta2/pelota_verde")
            colision_entre_objetos(str(nombre),str(raqueta1.rect.x),str(raqueta1.rect.y),"raqueta2","pelota","verde")
            
            #colision pelota roja
        if raqueta2.rect.colliderect(pelota_roja.rect):
            pelotava= True
            pelota_roja.dx = -1
            colisiones += 1
            colision_raqueta2 += 1
            
            archivo_colisiones(str(nombre),(f"{raqueta2.rect.x}/{raqueta2.rect.y}"),"raqueta2/pelota_roja")
            colision_entre_objetos(str(nombre),str(raqueta1.rect.x),str(raqueta1.rect.y),"raqueta2","pelota","roja")

        #colision entre pelota roja y verde
        if pelota_roja.rect.colliderect(pelota_verde.rect):
            colision_verde_rojo(str(nombre),pelota_roja.rect.x,pelota_roja.rect.y)
            


        if raqueta1.puntos==0:
            correrOno=False
        #grupo laser
        for laser in grupo_laser:
            if laser.rect.y<0:
                
                grupo_laser.remove(laser)
                todo_sprites.remove(laser)
                
        for impacto in grupo_laser:
            impacto_nave = pygame.sprite.spritecollide(pelota, grupo_laser,True)
            
        #aumento de velocidad de la pelota    
        if contador==100:
            pelota.velocidad += 1
            raqueta2.velocidad += 1
        if contador == 200:
            pelota.velocidad += 1
            raqueta1.velocidad += 1
        if contador == 300:
            raqueta2.velocidad += 1
            contador = 0
        if raqueta1.puntos == 0:
            admin_archivos.carga_historial_por_partida(str(nombre), str(raqueta2.puntos),colision_raqueta1,colision_raqueta2, str(colisiones))
        grupo_laser.update()
    # corre la funcion de reescritura
    #desde el bucle principar recibo el nombre del jugaror en la funcion de juego
    #para mostrar en pantalla
        
        juego(nombre,todo_sprites)