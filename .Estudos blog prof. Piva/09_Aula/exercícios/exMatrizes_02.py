matriz = [[0,0], [0,0]]   #linha, coluna

for i in range(2):
    for j in range(2):
        numero = int(input(f"Digite o número inteiro {i+1}|{j+1}: "))
        matriz[i][j] = numero

maior_elemento = matriz[0][0]
for i in range(2):
    for j in range(2):
        if matriz[i][j] > maior_elemento:
            maior_elemento = matriz[i][j]

# Multiplicar a matriz pelo maior elemento
for i in range(2):
    for j in range(2):
        matriz[i][j] *= maior_elemento

# Imprimir a matriz resultante
for i in range(2):
    for j in range(2):
        print(matriz[i][j], end=" ")
