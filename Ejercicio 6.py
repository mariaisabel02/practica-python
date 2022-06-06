# Ejercicio 6: Construya un programa que dibuje la siguiente figura en consola
# usando While o For o funciones.

#     *       4 espacios blancos, 1 asterisco
#    ***      3 espacios blancos, 3 asteriscos
#   *****     2 espacio blanco,   5 asteriscos
#  *******    1 espacios blancos, 7 asteriscos
# *********   0 espacios blancos, 9 asteriscos

def triangulo():
    hileraEspacios = ""
    hileraAsteriscos = ""
    cantidadEspacios = 4  # numero inicial de espacios en la primera fila

    for i in range(1, 9, 2):
        hileraAsteriscos = "*" * i
        hileraEspacios = " " * cantidadEspacios
        fila = hileraEspacios + hileraAsteriscos
        cantidadEspacios -= 1
        print(fila)


# *********  0 espacios blancos, 9 asteriscos
#  *******   1 espacio blanco,   7 asteriscos
#   *****    2 espacios blancos, 5 asteriscos
#    ***     3 espacios blancos, 3 asteriscos
#     *      4 espacios blancos, 1 asterisco

def trianguloInvertido():
    hileraEspacios = ""
    hileraAsteriscos = ""
    cantidadEspacios = 0  # los espacios corresponden al numero de fila

    for i in range(9, 0, -2):  # la cantidad de asteriscos disminuye en dos por cada fila
        hileraAsteriscos = "*" * i
        hileraEspacios = " " * cantidadEspacios
        fila = hileraEspacios + hileraAsteriscos
        cantidadEspacios += 1
        print(fila)


triangulo()
trianguloInvertido()
