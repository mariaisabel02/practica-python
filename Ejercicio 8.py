# Ejercicio 8: Calcule el área de un cuadrado de
# tamaño X dentro de m rectángulos. La diferencia del lado entre un
# cuadrado y su mayor inscrito es 2 unidades, así por ejemplo si el lado
# del cuadrado superior es 8 el próximo inscrito tendrá un tamaño de 6.
# Los valores de n y m son dados por el usuario y corresponden
# respectivamente al lado del cuadrado superior y la cantidad de
# cuadrados inscritos. Nota: n debe ser suficientemente grande como
# par meter todos lo m cuadrados y que el menor cuadrado tenga un lado
# de al menos una unidad.

def areaCuadradoInscrito():
    continuar = True

    while continuar:
        # cantidadCuadradosInscritos
        m = int(input("Escriba la cantidad de rectangulos inscritos: "))

        # ladoCuadradoSuperior
        n = int(input("Escriba el valor del lado del rectangulo superior: "))

        ladoCuadrado = n - (2 * m)

        if ladoCuadrado >= 1:
            #print("El valor del lado cabe en la cantidad de rectangulos")
            print("El area del cuadrado es " + str(ladoCuadrado*ladoCuadrado))
            continuar = False
        else:
            print("Escriba un lado mas grande para esa cantidad de rectangulos\n")

areaCuadradoInscrito()