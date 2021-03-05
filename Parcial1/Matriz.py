def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)


matriz = [
    [25, 69,],
    [68.5, 35]
]

mostrar_matriz(matriz)

filas = len(matriz)
columnas = len(matriz[0])
OperaL = 0
OperaC = 0

for i in range(filas):
    suma = sum(matriz[i])
    matriz[i].append(suma)
    OperaL = OperaL + 1

print()

mostrar_matriz(matriz)

print()

nueva_fila = []

for j in range(columnas):
    suma = sum([fila[j] for fila in matriz])
    nueva_fila.append(suma)
    OperaC = OperaC + 1

nueva_fila.append(sum(nueva_fila))

matriz.append(nueva_fila)

mostrar_matriz(matriz)

print (OperaC + OperaL)
