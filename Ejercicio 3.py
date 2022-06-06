# Ejercicio 3: Diseña un programa que resuelva la siguiente situación: Se van a
# distribuir tomates de 4 camiones en cajas de 8 kilos. ¿Cuántas cajas son necesarias para
# cada camión? Los camiones transportan las siguientes cantidades:
# - Camión uno: 3460 kilos.
# - Camión dos: 2800 kilos.
# - Camión tres: 1760 kilos.
# - Camión cuatro: 3535 kilos.


capacidadCaja = 8
cantidadCamiones = 4
capacidadCamiones = [3460, 2800, 1760, 3535]
cajasPorCamion = {}


for camion in range(4):
    maximoCajas = capacidadCamiones[camion] / 8
    cajasPorCamion.update({"camion "+str(camion):maximoCajas})

for camion in range(4):
    cantidad = cajasPorCamion["camion "+str(camion)]
    print("El camion " + str(camion+1) + " tiene capacidad para " + str(cantidad) + " cajas")


