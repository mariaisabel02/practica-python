# Ejercicio 2: Solicitar al usuario que ingrese números enteros positivos y, por
# cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se
# ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario
# fueron números pares.

detenerse = False
totalPares = 0


def sumarDigitos(numero):
    suma = 0
    for x in numero:
        suma = suma + int(x)
    print("La suma de los digitos de " + numero + " es: " + str(suma))


def esPar(numero):
    par = False
    if numero % 2 == 0:
        par = True
    return par


while not detenerse:
    numero = int(input("\nIngrese un numero positivo: "))

    if numero > -1:  # es positivo, asumiendo que cero tambien lo es
        sumarDigitos(str(numero))
        if esPar(numero): totalPares += 1

    elif numero == -1:
        detenerse = True
        print("El total de numeros pares es: " + str(totalPares))

    else:
        print("Por fovor ingrese solo numeros positivos o -1 para finalizar\n")
