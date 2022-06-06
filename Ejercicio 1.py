# Ejercicio 1: Leer números enteros de teclado, hasta que el usuario ingrese
# el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

detenerse = False
listaNumeros = []

def sumarPositivos():
    total = 0
    for x in listaNumeros:
        numero = listaNumeros[x]
        if numero > 0:
            total = total + numero
    return total


while not detenerse:
    numero = int(input("Ingrese un numero: "))
    if numero == 0:
        detenerse = True
        total = sumarPositivos()
        print("La suma de los numeros es: " + str(total))
    else:
        listaNumeros.append(numero)