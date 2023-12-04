from .pantallas import *

class PantallaControlador:  #Clase para controlar la ejecucion de las pantallas
    def __init__(self):
        self.menu = Menu()
        self.partida = Partida()
        #self.resultado = Resultado()
        self.record = Record()

    def start(self):
        valor = self.menu.bucle_pantalla()

        if valor == "partida":
            self.partida.bucle_fotograma()
            resultado_partida = self.partida.finalizacion_de_juego()
            self.resultado = Resultado(resultado_partida)
            self.resultado.bucle_pantalla()
        elif valor == "record":
            self.record.bucle_pantalla()
