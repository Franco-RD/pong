import pygame as pg
from pongapp.figura_class import *
from pongapp.utils import *



class Partida:  #Clase para generar pantallas
    def __init__(self):
        pg.init()
        pg.font.init()
        self.pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("PONG")
        self.tasa_refresco = pg.time.Clock() 

        self.pelota = Pelota(ANCHO//2, ALTO//2, COLOR_PELOTA)
        self.raqueta1 = Raqueta(0, ALTO//2)  #Raqueta izquierda
        self.raqueta2 = Raqueta(780, ALTO//2)  #raqueta derecha

    def bucle_fotograma(self):
        game_over = True

        while game_over:
            
            #Obtener la tasa de refrescos en ms
            self.valor_tasa = self.tasa_refresco.tick(600)  #Variable para controlar la velocidad entre fotogramas. A menor numero entre () mas lento es. No hace falta asignarlo a una variable si no se va a usar
            #print(valor_tasa)

            #Captura de eventos
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = False    
            
            #Seteo de pantalla, dibujo y movimiento de objetos
            self.pantalla_principal.fill(COLOR_PANTALLA)  #Color de pantalla
            pg.draw.line(self.pantalla_principal, COLOR_BLANCO, (ANCHO//2,0), (ANCHO//2,ALTO), width=10)  #Linea de mitad de cancha
            self.pelota.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)

            self.raqueta1.mover(pg.K_w, pg.K_s)
            self.raqueta2.mover(pg.K_UP, pg.K_DOWN)
            self.pelota.mover()

            #Colision
            self.pelota.comprobar_choqueV2(self.raqueta1, self.raqueta2)

            #Color del texto   
            self.pelota.mostrar_marcador(self.pantalla_principal)
            #jugador1 = jugador1_font.render("Jugador 1", True, (255,255,255))
            #jugador2 = jugador2_font.render("Jugador 2", True, (255,255,255))
            
            #Muestra de jugadores en marcadores
            #self.pantalla_principal.blit(jugador1, (310,10))
            #self.pantalla_principal.blit(jugador2, (430,10))
            

            pg.display.flip()
        pg.quit()