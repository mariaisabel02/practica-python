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
        return jugada


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
        return jugada


class PiedraPapelTijera():
    def __init__(self):
        self.opciones = ["piedra", "papel", "tijera"]
        self.jugadores = []

    def crearJugadores(self):
        print("Escriba quien sera cada jugador (humano o computadora)")

        for x in range(2):  # tenemos dos jugadores que pueden ser humanos o computadores
            entradaValida = False
            while not entradaValida:
                jugador = input("\nJugador " + str(x + 1) + ": ")

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
        continuar = True
        jugadaUsuario = ""
        jugadaComputador = ""
        jugada = ["",""]

        while continuar:
            for jugador in range(2):  # en cada turno juegan ambos jugadores

                jugadorActual = self.jugadores[jugador]
                print("\nEs el turno de " + jugadorActual.nombre)

                if jugadorActual.tipo == "usuario":
                    print(str(jugador))
                    jugada[jugador] = jugadorActual.jugar()
                else:
                    jugada[jugador] = jugadorActual.jugar(self.opciones)

                self.actualizarPuntaje(jugada[0], jugada[1])

            seguir = input("\nEscriba continuar para volver a jugar o salir para terminar: ")
            if seguir != "continuar": continuar = False

        self.determinarGanador()

    def actualizarPuntaje(self, jugada1, jugada2):  # recibe jugadas de ambos participantes en el turno actual
        # jugaron lo mismo y suma un punto
        print("Las jugadas fueron: " + jugada1 + " - " + jugada2)

        if jugada1 == jugada2:
            self.jugadores[0].puntaje += 1
            self.jugadores[1].puntaje += 1
            print("Ambos obtienen un punto")

        # piedra papel
        elif jugada1 == "piedra" and jugada2 == "papel":
            print("3 puntos para " + self.jugadores[1].nombre)
            self.jugadores[1].puntaje += 3

        elif jugada2 == "piedra" and jugada1 == "papel":
            print("3 puntos para " + self.jugadores[0].nombre)
            self.jugadores[0].puntaje += 1

        # papel tijera
        elif jugada1 == "papel" and jugada2 == "tijera":
            print("3 puntos para " + self.jugadores[1].nombre)
            self.jugadores[1].puntaje += 3

        elif jugada2 == "papel" and jugada1 == "tijera":
            print("3 puntos para " + self.jugadores[0].nombre)
            self.jugadores[0].puntaje += 1


        # tijera piedra
        elif jugada1 == "tijera" and jugada2 == "piedra":
            print("3 puntos para " + self.jugadores[1].nombre)
            self.jugadores[1].puntaje += 3

        elif jugada2 == "tijera" and jugada1 == "piedra":
            print("3 puntos para " + self.jugadores[0].nombre)
            self.jugadores[1].puntaje += 1

    def determinarGanador(self):
        puntajeJugador1 = self.jugadores[0].puntaje
        puntajeJugador2 = self.jugadores[1].puntaje

        if puntajeJugador1 < puntajeJugador2:
            print("Felicidades al ganador:" + self.jugadores[1].nombre)
        elif puntajeJugador1 > puntajeJugador2:
            print("Felicidades al ganador:" + self.jugadores[0].nombre)
        else:
            print("Ambos jugadores empataron!")

juego = PiedraPapelTijera()
juego.crearJugadores()
juego.iniciarJuego()
