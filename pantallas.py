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

        #self.fuente = pg.font.SysFont("verdana", 30)  #SysFont toma fuentes del sistema   
        self.fuente = pg.font.Font(None,30)  #Font toma fuentes de un archivo que las contenga

        self.contadorDerecho = 0
        self.contadorIzquierdo = 0
        self.quienMarco = ""
    
    def bucle_fotograma(self):
        game_over = True

        while game_over:
            
            #Obtener la tasa de refrescos en ms
            self.valor_tasa = self.tasa_refresco.tick(600)  #Variable para controlar la velocidad entre fotogramas. A menor numero entre () mas lento es. No hace falta asignarlo a una variable si no se va a usar
            #print(self.valor_tasa)

            #Captura de eventos
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = False    
            
            #Seteo de pantalla, dibujo y movimiento de objetos
            self.pantalla_principal.fill(COLOR_PANTALLA)  #Color de pantalla
            self.mostrar_linea_central()

            self.pelota.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)
            self.mostrar_jugadores()

            self.raqueta1.mover(pg.K_w, pg.K_s)
            self.raqueta2.mover(pg.K_UP, pg.K_DOWN)   

            self.mostrar_marcador()
            

            #Colision
            self.pelota.comprobar_choqueV2(self.raqueta1, self.raqueta2)

             
            #self.pelota.mostrar_marcador(self.pantalla_principal)  ahora esta en esta misma clase
                      

            pg.display.flip()
        pg.quit()

    def mostrar_linea_central(self):
        for cont_linea in range(0,601,70):
            pg.draw.line(self.pantalla_principal, COLOR_BLANCO, (ANCHO//2,cont_linea), (ANCHO//2,cont_linea+50), width=10)

    def mostrar_jugadores(self):                     
        jugador1 = self.fuente.render("Jugador 1", True, COLOR_AZUL)
        jugador2 = self.fuente.render("Jugador 2", True, COLOR_NARANJA)        
        self.pantalla_principal.blit(jugador1, (295,10))
        self.pantalla_principal.blit(jugador2, (410,10))

    def mostrar_marcador(self):
        self.quienMarco = self.pelota.mover()  #Se asigna el return str del metodo mover del objeto Pelota a una variable para ver quien metio un punto y utilizar el contador en esta clase. 
        if self.quienMarco == "right":
            self.contadorDerecho += 1
        elif self.quienMarco == "left":
            self.contadorIzquierdo += 1    

        marcador1 = self.fuente.render(str(self.contadorDerecho), True, COLOR_AZUL)  #El .render  devuelve un objeto de tipo surface, que muestra un str seteado con demas parametros
        marcador2 = self.fuente.render(str(self.contadorIzquierdo), True, COLOR_NARANJA)        
        self.pantalla_principal.blit(marcador1, (335,35))  #Blit muestra un objeto de tipo surface en una coordenada
        self.pantalla_principal.blit(marcador2, (450,35))