# Ejercicio 4: Diseña un programa que, a partir del valor de la base y de la
# altura de un triangulo (ej. 3 y 5 metros, respectivamente), muestre el valor de su área (en
# metros cuadrados). Recuerda que el área A de un triángulo se puede calcular a partir de la
# base b y la altura h como A = 1/2 b*h

base = int(input("Digite la base: "))
altura = int(input("Digite la altura: "))

area = (base*altura)/2
print("El area del triangulo es: "+str(area)+" metros cuadrados")