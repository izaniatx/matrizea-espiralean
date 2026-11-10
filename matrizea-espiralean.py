def espiral(matriz):
    resultado = []
    arriba, abajo = 0, len(matriz) - 1
    izq, der = 0, len(matriz[0]) - 1

    while arriba <= abajo and izq <= der:
        for j in range(izq, der + 1):
            resultado.append(matriz[arriba][j])
        arriba += 1

        for i in range(arriba, abajo + 1):
            resultado.append(matriz[i][der])
        der -= 1

        if arriba <= abajo:
            for j in range(der, izq - 1, -1):
                resultado.append(matriz[abajo][j])
            abajo -= 1

        if izq <= der:
            for i in range(abajo, arriba - 1, -1):
                resultado.append(matriz[i][izq])
            izq += 1

    return resultado


m = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]

print(espiral(m))  # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]