# Ejercicio 5: Cree un programa que dado un número determine si es un
# número primo o no. Recuerde los números primos son aquello que solo son divisibles por 1 y
# por ellos mismos.

terminar = False

print("Bienvenido al programa que determina numeros primos. Para salir digite 'no'")
while not terminar:
    numero = input("\nIngrese un numero: ")
    esPrimo = True
    if not numero.isdigit():
        terminar = True
    else:
        numero = int(numero)
        if numero != 1:
            for x in range(2, numero-1):
                if numero % x == 0:
                    esPrimo = False
        print("Es primo "+str(esPrimo))