import pygame as pg
from figura_class import *

pg.init()

#Definicion de la pantalla
pantalla_principal = pg.display.set_mode((800, 600))
pg.display.set_caption("PONG")

tasa_refresco = pg.time.Clock()  #Definir un objeto tipo clock para poder configurar una tasa de refresco en nuestro bucle de fotogramas. 


#Agregar marcadores
#Fuente y tamaño de letra
#marcador1_font = pg.font.SysFont("verdana", 30)  #SysFont toma parametros del sistema
#marcador2_font = pg.font.SysFont("verdana", 30)
marcador1_font = pg.font.Font(None, 30)  #Font toma fuentes de un archivo que las contenga
marcador2_font = pg.font.Font(None, 30)

jugador1_font = pg.font.SysFont("verdana", 10,True)
jugador2_font = pg.font.SysFont("verdana", 10,True)



#Definicion de objetos para el juego
pelota = Pelota(400, 300, (228,231,19), 10)
raqueta1 = Raqueta(10, 300)  #Raqueta izquierda
raqueta2 = Raqueta(790, 300)  #raqueta derecha


#Bucle del juego principal, el juego corre hasta que se toca cerrar
game_over = True

while game_over:
    
    #Obtener la tasa de refrescos en ms
    valor_tasa = tasa_refresco.tick(600)  #Variable para controlar la velocidad entre fotogramas. A menor numero entre () mas lento es. No hace falta asignarlo a una variable si no se va a usar
    #print(valor_tasa)


    #Captura de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = False    
    

    #Seteo de pantalla, dibujo y movimiento de objetos
    pantalla_principal.fill((27,149,47))  #Color de pantalla
    pg.draw.line(pantalla_principal, (255, 255, 255), (400,0), (400, 600), 15)  #Linea de mitad de cancha
    pelota.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)

    raqueta1.mover(pg.K_w, pg.K_s)
    raqueta2.mover(pg.K_UP, pg.K_DOWN)
    pelota.mover()
    

    #Color del texto   
    pelota.mostrar_marcador(pantalla_principal)
    jugador1 = jugador1_font.render("Jugador 1", True, (255,255,255))
    jugador2 = jugador2_font.render("Jugador 2", True, (255,255,255))
    
    #Muestra de marcadores
    pantalla_principal.blit(jugador1, (310,10))
    pantalla_principal.blit(jugador2, (430,10))
    

    pg.display.flip()

pg.quit()

