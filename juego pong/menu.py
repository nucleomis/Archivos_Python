#----------------------importaciones-------------------------------------------

import sys,random
import pygame,pong,read_data
from admin_archivos import records

#-------------------------GLOBALES-----------------------------------------------
pygame.init()

ventana= pygame.display.set_mode((750,500))


pygame.display.set_caption('tp programacion')

blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0,255,0)
azul = (0, 0, 255)
naranja = (255,125,0)

carga_jugador  = read_data.Jugador()


pos_opciones = 100

todo_sprites = pygame.sprite.Group()


#--------------------------------------------------------------------------


class Grilla(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([290, 80])
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        


class Opciones(pygame.sprite.Sprite):
    def __init__(self,valor,pos_x,pos_y,color):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont('Comic Sans MS', 30)    
        self.text = self.font.render(valor, False, color)
        self.textRect = self.text.get_rect()
        self.textRect.center = (pos_x, pos_y)
        ventana.blit(self.text, self.textRect)


class Record():
    def __init__(self):
        self.top = records()
        # pone la pantalla en negro
        ventana.fill(negro)
        # Fuente del titulo
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        #subtitulo con el nombre del juego
        self.text2 = self.font.render('RECORDS:', False, rojo)
        self.textRect2 = self.text2.get_rect()
        self.textRect2.center = (750 // 2, 20)
        #opciones del menu
        self.opcion0 = Opciones(f"1){self.top[0][0]}-puntos:{self.top[0][1]} *Fecha:{self.top[0][2]}", 350, 80,verde)
        self.opcion1 = Opciones(f"2){self.top[1][0]}-puntos:{self.top[1][1]} *Fecha:{self.top[1][2]}", 350, 120,azul)
        self.opcion2 = Opciones(f"3){self.top[2][0]}-puntos:{self.top[2][1]} *Fecha:{self.top[2][2]}", 350, 160,azul)
        self.opcion3 = Opciones(f"4){self.top[3][0]}-puntos:{self.top[3][1]} *Fecha:{self.top[3][2]}", 350, 200,azul)
        self.opcion4 = Opciones(f"5){self.top[4][0]}-puntos:{self.top[4][1]} *Fecha:{self.top[4][2]}", 350, 240,azul)
        self.opcion5 = Opciones(f"6){self.top[5][0]}-puntos:{self.top[5][1]} *Fecha:{self.top[5][2]}", 350, 280,azul)
        self.opcion6 = Opciones(f"7){self.top[6][0]}-puntos:{self.top[6][1]} *Fecha:{self.top[6][2]}", 350, 320,azul)
        self.opcion7 = Opciones(f"8){self.top[7][0]}-puntos:{self.top[7][1]} *Fecha:{self.top[7][2]}", 350, 360,azul)
        self.opcion8 = Opciones(f"9){self.top[8][0]}-puntos:{self.top[8][1]} *Fecha:{self.top[8][2]}", 350, 400,azul)
        self.opcion9 = Opciones(f"10){self.top[9][0]}-puntos:{self.top[9][1]} *Fecha:{self.top[9][2]}", 350, 440,rojo)
        self.opcion11 = Opciones(" ESCAPE PARA SALIR",240+130,425+50,verde)

        ventana.blit(self.text2, self.textRect2)
        pygame.draw.line(ventana, azul, (0,60),(750,60), 2)

    
    def correr_menu(self, encenderOno):
        self.pos = 0
        Record().__init__()
        while encenderOno:
            pygame.time.delay(60)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()
            
            self.tecla = pygame.key.get_pressed()

            #opcion para cargar el jugador si no existe
            if self.pos == 0 and self.tecla[pygame.K_ESCAPE]:
                encenderOno=False
                return False
            pygame.display.update()




class Menu():

    def __init__(self):
        self.pos_x_grilla = 235
        self.pos_y_grilla = 140
        self.recuadro = Grilla ()
        todo_sprites.add(self.recuadro)
        self.juego = pong
        # pone la pantalla en negro
        ventana.fill(negro)

        # Fuente del titulo
        todo_sprites.draw(ventana)
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        #titulo de la ventana
        self.text1 = self.font.render('TP: Pin Pong', False, azul)
        self.textRect1 = self.text1.get_rect()
        self.textRect1.center = (750 // 2, 25)
        #subtitulo con el nombre del juego
        self.text2 = self.font.render('JUEGO DE PONG:', False, naranja)
        self.textRect2 = self.text2.get_rect()
        self.textRect2.center = (750 // 2, 100)
        #opciones del menu
        self.opcion0 = Opciones("JUGADOR NUEVO", 240+130, 135+50,verde)
        self.opcion1 = Opciones("JUGAR",240+130,235+50,verde)
        self.opcion2 = Opciones("RECORDS",240+130,335+50,verde)
        self.opcion3 = Opciones("SALIR",240+130,425+50,rojo)

        ventana.blit(self.text1, self.textRect1)
        ventana.blit(self.text2, self.textRect2)
        pygame.draw.line(ventana, azul, (0,60),(750,60), 2)
        pygame.draw.line(ventana, naranja, (240,120),(500,120), 2)

        

    def correr_menu(self, encenderOno):
        self.pos = 0
        self.recuadro.rect.x = 225
        self.recuadro.rect.y = 150
        pygame.draw.rect(self.recuadro.image,blanco,(0,0,290,80),4)
        rec = Record
        
        while encenderOno:
            ventana.fill(negro)
            pygame.time.delay(60)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()
            
            self.tecla = pygame.key.get_pressed()

            #opcion para cargar el jugador si no existe
            if self.pos == 0 and self.tecla[pygame.K_SPACE]:
                verdad = carga_jugador.correr_menu_carga()
                if verdad == False: 
                    encenderOno = True

            if self.pos == 1 and self.tecla[pygame.K_SPACE]:#opcion para ingresar al login del juego
                self.login = carga_jugador.login()
                if self.login[0]:
                    pong.main(self.login[0],self.login[1])   
                
            if self.pos ==2 and self.tecla[pygame.K_SPACE]:
                encenderOno = False
                verdad = rec().correr_menu(True)
                if verdad == False:
                    self.correr_menu (True)

            #opcion evento para salir de juego
            if self.tecla[pygame.K_SPACE] and  self.pos == 3:
                sys.exit()

            #opcion para subir el recudro
            if self.tecla[pygame.K_w]:
                if self.pos >0 or self.pos <4:
                    self.pos += -1
                    self.recuadro.rect.y += -pos_opciones
                    if self.pos == -1:
                        self.recuadro.rect.y = self.recuadro.rect.y+400
                        self.pos = 3
            
            #mover el recuadro para abajo 
            if self.tecla[pygame.K_s]:
                if self.pos >0 or self.pos <4:
                    self.pos += 1
                    self.recuadro.rect.y += pos_opciones
                    if self.pos == 4:
                        self.recuadro.rect.y = self.recuadro.rect.y-400
                        self.pos = 0
            Menu().__init__()
            pygame.display.update()
