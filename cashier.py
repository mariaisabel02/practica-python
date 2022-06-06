# clase que maneja los montos (lectura y validación)
class Montos():
    def leerMonto(self):
        montoValido = False
        monto = None

        while not montoValido:
            try:
                monto = int(input("escriba el monto: "))
                montoValido = self.validarMonto(monto)

                if not montoValido: print("El monto ingresado no es válido. Escriba otro monto.")

            except ValueError:
                print("La transacción falló.")

        return monto

    def validarMonto(self, montoIngresado):
        if self.esEntero(montoIngresado) & self.estaEnRangoValido(montoIngresado):
            return True
        else:
            return False

    def esEntero(self, montoIngresado):
        entero = isinstance(montoIngresado, int)
        if not entero: print("El monto debe ser un entero.")
        return entero

    def estaEnRangoValido(self, montoIngresado):
        if montoIngresado < 2000:
            return False
        elif 2000 < montoIngresado < 5000 or 5000 > montoIngresado > 10000:
            return False
        else:
            return True


# clase que calcula el cambio en billetes para devolver al usuario
class Cambio:
    def __init__(self, monto):
        self.billetes = [10000, 5000, 2000]  # posibles billetes a utilizar
        self.monto = monto  # monto solicitado
        self.listaBilletes = {10000: 0, 5000: 0, 2000: 0}  # billetes dados al usuario

    # determina los billetes que se daran al usuario
    def calcularCambio(self):
        i = 0
        resto = self.monto

        while resto != 0 & i < 2:  # mientras no se haya completado el monto y no se acabe la lista de billetes

            billete = self.billetes[i]  # billete actual en la lista de billetes

            while resto >= billete:  # mientras me alcance con ese billete lo agrego al cambio
                self.listaBilletes[billete] = self.listaBilletes[billete] + 1
                resto = resto - billete

            i += 1  # paso al siguiente billete
            if i == 3:  # solo hay tres billetes, entonces la transaccion fallo
                print("La transaccion falló. No es posible dar el monto con los billetes disponibles.")
                return False

        return True

    # imprime el cambio del usuario de acuerdo con la cantidad de billetes por denominacion
    def leerCambio(self):
        for key in range(0, len(self.listaBilletes)):  # recorrido de la lista de billetes que se le dieron como cambio
            billete = self.billetes[key]
            cantidad = self.listaBilletes[billete]
            print(str(cantidad) + " billetes de " + str(billete))


class Bitacora():
    def leerBitacora(self):
        with open('archivo.csv', 'r') as archivo:
            for linea in archivo:
                print(repr(linea))

    def escribirBitacora(self, monto, transaccion):
        with open('archivo.csv', 'a') as archivo:
            archivo.write("Monto: "+ str(monto) + " cambio: " + str(transaccion)+"\n")


class Cajero():

    def __init__(self):
        iniciar = int(input("Escriba 1 para solicitar dinero, 2 para ver la bitacora, 3 para salir: "))

        if iniciar == 1:
            self.realizarTransaccion()
            self.__init__()

        elif iniciar == 2:
            usuarioValidado = self.autenticarUsuario()
            if usuarioValidado:
                self.leerBitacora()
            else:
                print("Usuario o contrasena invalidos.")
            self.__init__()

        elif iniciar == 3:
            print("Gracias por usar el cajero!")

        else:
            print("Solicitud no valida.")
            self.__init__()

    def realizarTransaccion(self):
        iniciar = "si"
        while iniciar == "si":

            # lectura y validacion del monto
            monto = Montos()
            montoSolicitado = monto.leerMonto()

            # calculo del cambio necesario para cubir el monto
            cajero = Cambio(montoSolicitado)
            seRealizoTransaccion = cajero.calcularCambio()

            if seRealizoTransaccion: # si fue posible realizar la transaccion
                cajero.leerCambio()
                bitacora = Bitacora()
                bitacora.escribirBitacora(montoSolicitado, cajero.listaBilletes)

            iniciar = input("Desea realizar otra transaccion? si o no: ")

    def leerBitacora(self):
        bitacora = Bitacora()
        bitacora.leerBitacora()

    def autenticarUsuario(self):
        usuarioAutorizado = "admin"
        contrasenaAutorizada = "admin"

        usuario = input("Ingrese su usuario: ")
        contrasena = input("Ingrese su contrasena: ")

        if usuario == usuarioAutorizado and contrasena == contrasenaAutorizada:
            return True
        else:
            return False


print("Bienvenido al cajero.")
cajero = Cajero()
