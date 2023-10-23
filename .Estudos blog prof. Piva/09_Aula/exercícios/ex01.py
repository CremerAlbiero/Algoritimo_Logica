#criar vetor com 10 elementos. Imprimir ao contrário da ordem inserida.
vetor = []

for i in range(1, 11):
    valor = int(input(f"Digite o número {i}: "))
    vetor.append(valor)
print(vetor[::-1])