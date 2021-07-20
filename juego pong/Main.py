import menu, pong, pygame
import random, sys


ventana= pygame.display.set_mode((750,500))


pygame.display.set_caption('tp programacion')
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0,255,0)
azul = (0, 0, 255)
naranja = (255,125,0)
pygame.init()
#------------------------------------------------------------------
#          Booleanos para correr el juego
jugar = True

corre_menu = True



class Game_Over():
    def __init__(self):
        self.tecla = pygame.key.get_pressed()
        if self.tecla[pygame.K_SPACE]:
            self.continuar=True
        else:
            self.continuar=False  
        
        
        if self.continuar==False:
            pygame.time.delay(100)
            self.cambio = random.randrange(1,3)
            
            if self.cambio == 1:
                self.color = rojo
            else: 
                self.color = blanco
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()
            ventana.fill(negro)
            self.font1 = pygame.font.SysFont('Comic Sans MS', 90)
            self.text1 = self.font1.render('FIN DEL JUEGO', False, self.color)
            self.textRect1 = self.text1.get_rect()
            self.textRect1.center = (750 // 2, 225)
            ventana.blit(self.text1, self.textRect1)

            self.font2 = pygame.font.SysFont('Arial', 30)
            self.text2 = self.font2.render(' presione "espacio" para volver al menu', False, blanco)
            self.textRect2 = self.text2.get_rect()
            self.textRect2.center = (750 // 2, 325)
            ventana.blit(self.text2, self.textRect2)
            pygame.display.update()

#------------------------------------------------------------------
#       bucle principal del juego

   
while jugar:
    menu.Menu().correr_menu(corre_menu)
    if pong.raqueta1.puntos==0:
        corre_menu = False 
        Game_Over()
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_SPACE]:
            corre_menu = True
            pong.raqueta1.puntos = 10
            pong.raqueta1.velocidad = 10
            pong.raqueta2.puntos = 0
            pong.raqueta2.velocidad = 10
            pong .pelota.velocidad = 11
            pong.col = 0