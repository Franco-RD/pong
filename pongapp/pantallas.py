import pygame as pg
from pongapp.figura_class import *
from pongapp.utils import *



class Partida:  #Clase para generar pantalla de partida
    def __init__(self):
        
        #pg.font.init()
        self.pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("PONG")
        self.tasa_refresco = pg.time.Clock()  #Variabla para tasa de refresco

        #Declaracion de objetos del juego
        self.pelota = Pelota(ANCHO//2, ALTO//2, COLOR_PELOTA)
        self.raqueta1 = Raqueta(0, ALTO//2)  #Raqueta izquierda
        self.raqueta2 = Raqueta(780, ALTO//2)  #raqueta derecha

        #self.fuente = pg.font.SysFont("verdana", 30)  #SysFont toma fuentes del sistema   
        self.fuente = pg.font.Font(FUENTE1,SIZE_FUENTE_1)  #Font toma fuentes de un archivo que las contenga (en este caso la ruta esta en una variable), o None para que vaya con una predeterminada
        self.fuenteTwo = pg.font.Font(FUENTE2,SIZE_FUENTE_1)
        self.contadorDerecho = 0
        self.contadorIzquierdo = 0
        self.quienMarco = ""

        self.game_over = True
        self.temporizador = TIEMPO_JUEGO #En milisegundos

        self.contadorFotograma = 0
        self.colorFondo = COLOR_PANTALLA

        self.resultado_partida = ""

    def bucle_fotograma(self):    
        #Iniciar las variables al principio de la partida para reiniciar sus valores luego de cada juego
        self.temporizador = TIEMPO_JUEGO   
        self.tasa_refresco.tick()
        self.contadorDerecho = 0
        self.contadorIzquierdo = 0

        while self.game_over and (self.contadorDerecho < 7 or self.contadorIzquierdo < 7) and self.temporizador > 0:
            
            #Obtener la tasa de refrescos en ms
            self.valor_tasa = self.tasa_refresco.tick(VELOCIDAD_JUEGO)  #Variable para controlar la velocidad entre fotogramas. A menor numero entre () mas lento es. No hace falta asignarlo a una variable si no se va a usar
            #print(self.valor_tasa)   

            self.temporizador -= self.valor_tasa  

            #Captura de eventos
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    #self.game_over = False     
                    return True
            

            #Seteo de pantalla, dibujo y movimiento de objetos
            #self.pantalla_principal.fill(self.fijar_fondo())       
            self.fijar_fondo()   
            self.mostrar_linea_central()

            #Dibujo de objetos y nombres de jugadores
            self.pelota.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)
            self.mostrar_jugadores()

            #Movimiento
            self.raqueta1.mover(pg.K_w, pg.K_s)
            self.raqueta2.mover(pg.K_UP, pg.K_DOWN)  

            #Colision
            self.pelota.comprobar_choqueV2(self.raqueta1, self.raqueta2)    
            
            self.mostrar_marcador()   
            self.mostrar_temporizador() 
            
            self.finalizacion_de_juego()                  

            pg.display.flip()
            
        return self.resultado_partida
        

    def mostrar_linea_central(self):
        for cont_linea in range(0,ALTO+1,70):
            pg.draw.line(self.pantalla_principal, COLOR_BLANCO, (ANCHO//2,cont_linea), (ANCHO//2,cont_linea+50), width=10)

    def mostrar_jugadores(self):                     
        jugador1 = self.fuente.render("Jugador 1", True, COLOR_AZUL)
        jugador2 = self.fuente.render("Jugador 2", True, COLOR_VERDE)        
        self.pantalla_principal.blit(jugador1, (250,10))
        self.pantalla_principal.blit(jugador2, (420,10))

    def mostrar_marcador(self):
        self.quienMarco = self.pelota.mover()  #Se asigna el return str del metodo mover del objeto Pelota a una variable para ver quien metio un punto y utilizar el contador en esta clase. 
        if self.quienMarco == "right":
            self.contadorDerecho += 1
        elif self.quienMarco == "left":
            self.contadorIzquierdo += 1    

        marcador1 = self.fuenteTwo.render(str(self.contadorDerecho), True, COLOR_AZUL)  #El .render  devuelve un objeto de tipo surface, que muestra un str seteado con demas parametros
        marcador2 = self.fuenteTwo.render(str(self.contadorIzquierdo), True, COLOR_VERDE)        
        self.pantalla_principal.blit(marcador1, (305,35))  #Blit muestra un objeto de tipo surface en una coordenada
        self.pantalla_principal.blit(marcador2, (475,35))

    def finalizacion_de_juego(self):    
        #Finalizacion del juego por tiempo         
        if self.temporizador <= 0:
            print("Fin del juego")
            #self.game_over = False 

            if self.contadorDerecho > self.contadorIzquierdo:
                self.resultado_partida = f"Gana Jugador 1 - Resultado Jugador 1: {self.contadorDerecho} - Jugador 2: {self.contadorIzquierdo}"
            elif self.contadorDerecho < self.contadorIzquierdo:     
                self.resultado_partida = f"Gana Jugador 2 - Resultado Jugador 1: {self.contadorDerecho} - Jugador 2: {self.contadorIzquierdo}"
            else:
                self.resultado_partida = f"Empate - Resultado Jugador 1: {self.contadorDerecho} - Jugador 2: {self.contadorIzquierdo}"

        #Finalizacion de juego por puntos
        if self.contadorDerecho == 7:
            #self.game_over = False  
            self.resultado_partida = f"Gana Jugador 1 - Resultado Jugador 1: {self.contadorDerecho} - Jugador 2: {self.contadorIzquierdo}"
        if self.contadorIzquierdo == 7:
            #self.game_over = False
            self.resultado_partida = f"Gana Jugador 2 - Resultado Jugador 1: {self.contadorDerecho} - Jugador 2: {self.contadorIzquierdo}"
    
    def mostrar_temporizador(self):
        self.tiempo_juego = self.fuente.render(str(self.temporizador//1000), True, COLOR_ROJO)
        self.pantalla_principal.blit(self.tiempo_juego, (395,10))
    
    def fijar_fondo(self):
        
        if self.temporizador < TIEMPO_LIMIT_1 and self.temporizador > TIEMPO_LIMIT_2:
            self.pantalla_principal.fill(FONDO_NARANJA)
        elif self.temporizador < TIEMPO_LIMIT_2:
            self.pantalla_principal.fill(FONDO_ROJO)
        else: 
            self.pantalla_principal.fill(COLOR_PANTALLA)  #Color de pantalla   
        '''
        self.contadorFotograma += 1

        if self.temporizador > TIEMPO_LIMIT_1:
            self.contadorFotograma = 0
        elif self.temporizador > TIEMPO_LIMIT_2:
            if self.contadorFotograma == 20:  #Achicar el numero hace que el parpadeo sea mas rapido
                if self.colorFondo == COLOR_PANTALLA:
                    self.colorFondo = COLOR_NARANJA
                else:
                    self.colorFondo = COLOR_PANTALLA
                self.contadorFotograma = 0
        else:
            if self.contadorFotograma == 20:
                if self.colorFondo == COLOR_PANTALLA:
                    self.colorFondo = COLOR_ROJO
                else: 
                    self.colorFondo = COLOR_PANTALLA
                self.contadorFotograma = 0
        
        return self.colorFondo
        '''

class Menu:    
    def __init__(self):
        
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption('Menu')
        self.tasa_refresco = pg.time.Clock()

        self.imagenFondo = pg.image.load(IMGFONDO)  #Carga una imagen desde una ruta en una variable dandole el tipo Surface

        self.fuente = pg.font.Font(FUENTE1,SIZE_FUENTE_2)

        self.sonido = pg.mixer.Sound(SONIDO_MENU)

    def bucle_pantalla(self):
        game_over = True
        pg.mixer.Sound.play(self.sonido)
        while game_over:
            
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    pg.mixer.Sound.stop(self.sonido)
                    #game_over = False
                    return True
            
            #Registra si se toca enter y retorna el str partida si lo hace para pasar a la pantalla siguiente en main. Si toca r retorta record para ir a la pantalla da records en el main.              
            self.botones = pg.key.get_pressed()
            if self.botones[pg.K_RETURN]:
                pg.mixer.Sound.stop(self.sonido)
                return "partida"
            elif self.botones[pg.K_r]:
                pg.mixer.Sound.stop(self.sonido)
                return "record"

            self.pantalla_principal.blit(self.imagenFondo, (0,0))  #Carga la imagen de self.imagenFondo a la pantalla principal

            texto_menu = self.fuente.render("Pulsa ENTER para jugar", True, COLOR_AMARILLO)            
            self.pantalla_principal.blit(texto_menu, (200, ALTO//2))

            texto_record = self.fuente.render("Pulsa R para mostrar records", True, COLOR_AMARILLO)            
            self.pantalla_principal.blit(texto_record, (130, 400))

            pg.display.flip()

class Resultado:    
    def __init__(self):
        
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption('Resultado')
        self.tasa_refresco = pg.time.Clock()

        self.fuenteResultado = pg.font.Font(FUENTE1, SIZE_FUENTE_3)
        self.resultado = ""

    def bucle_pantalla(self):
        game_over = True
        while game_over:
            
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    #game_over = False
                    return False  #Con el return True lo que haria es que el boton de cerrar de la pantalla de resultados cerraria el juego. Como por ahora no podemos hacer que tocando enter vuelva
                                  #al menu, ponemos que retorne False asi sigue el bucle del controlador. Esto quiere decir que no se puede cerrar el juego desde la pantalla de resultados.
            
            """
            botones = pg.key.get_pressed()            
            if botones[pg.K_RETURN]:                
                break
            """

            self.pantalla_principal.fill(COLOR_BLANCO)
            mostrarResultado = self.fuenteResultado.render(self.resultado, True, COLOR_GRANATE)
            self.pantalla_principal.blit(mostrarResultado, (100, ALTO//2))


            pg.display.flip()

            
    def cargar_resultado(self, resultado):
        self.resultado = resultado
            
class Record:    
    def __init__(self):
        
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption('Puntajes')
        self.tasa_refresco = pg.time.Clock()       

        self.fuenteRecord = pg.font.Font(FUENTE1,SIZE_FUENTE_2) 

    def bucle_pantalla(self):
        game_over = True
        while game_over:
            
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    #game_over = False
                    return True

            self.botones = pg.key.get_pressed()
            if self.botones[pg.K_RETURN]:
                return "menu"
            
            
            self.pantalla_principal.fill(COLOR_BLANCO)
            texto = self.fuenteRecord.render("Mejores Puntajes", 0, COLOR_GRANATE)
            self.pantalla_principal.blit(texto, (160, ALTO//2))

            pg.display.flip()

        
            
