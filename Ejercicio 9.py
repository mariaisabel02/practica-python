# Ejercicio 9: Cree un juego que permita jugar piedra papel o tijera, tanto con
# usuarios humanos o como máquinas, los jugadores tienen puntajes que se deben guardar en
# un archivo de texto cada vez que termina un juego actualizando los marcadores, cada juego
# da 1 punto si empatan y 3 puntos si ganan al jugador.
# Al iniciar el programa debe preguntarle al usuario si desea jugar con máquinas o con
# humanos, el usuario debe escoger para los 2 jugadores el tipo de jugador que desea, así se
# pueden tener combinaciones como : Humano vrs Humano, Computador vrs Computador,
# Computador vrs Humano y Humano vrs Computador. Además el usuario debe asignarle un
# nombre al jugador. Al finalizar cada partida el usuario debe escoger si desea volver a jugar o
# salir

import random


class JugadorUsuario():
    def __init__(self, nombre):
        self.nombre = nombre
        self.tipo = "usuario"
        self.puntaje = 0
        self.jugadas = []

    def jugar(self):
        jugada = input("Indique su jugada. Escriba piedra, papel o tijera: ")
        self.jugadas.append(jugada)


class JugadorComputador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.tipo = "computador"
        self.puntaje = 0
        self.jugadas = []

    def jugar(self, opciones):
        aleatorio = random.randrange(0, 3)
        jugada = opciones[aleatorio]
        self.jugadas.append(jugada)


class PiedraPapelTijera():
    def __init__(self):
        self.opciones = ["Piedra", "Papel", "Tijera"]
        self.jugadores = []

    def crearJugadores(self):
        print("Escriba quien sera cada jugador (humano o computadora)")

        for x in range(2):  # tenemos dos jugadores que pueden ser humanos o computadores
            entradaValida = False
            while not entradaValida:
                jugador = input("Jugador " + str(x + 1) + ": ")

                if jugador == "humano":
                    entradaValida = True
                    nombre = input("Digite el nombre del jugador " + str(x + 1) + ": ")
                    self.jugadores.append(JugadorUsuario(nombre))

                elif jugador == "computadora":
                    entradaValida = True
                    self.jugadores.append(JugadorComputador("Computador " + str(x)))

                else:
                    print("Por favor escriba 'humano' o 'computadora'")

    def iniciarJuego(self):
        for jugador in range(2):
            jugadorActual = self.jugadores[jugador]
            print("Es el turno de " + jugadorActual.nombre)
            if jugadorActual.tipo == "usuario":
                jugadorActual.jugar()
            else:
                jugadorActual.jugar(self.opciones)

    def actualizarPuntaje(self):
        pass

    def determinarGanador(self):
        pass


juego = PiedraPapelTijera()
juego.crearJugadores()
juego.iniciarJuego()
