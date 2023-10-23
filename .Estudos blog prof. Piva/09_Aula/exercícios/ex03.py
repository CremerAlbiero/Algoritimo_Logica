vetor1 = []
vetor2 = []
vetor3 = []
for i in range(1, 11):
    num1 = int(input(f"Digite o número do primeiro vetor {i}: "))
    vetor1.append(num1)
    num2 = int(input(f"Digite o número do segundo vetor {i}: "))
    vetor2.append(num2)
    vetor3.append(num1)
    vetor3.append(num2)
print(f"O resultado da combinação dos dois vetores é: {vetor3}")

#exercicio: criar dois vetores de 10 elementos numericos. Mostrar um 3º vetor resultante na concatenação desses dois.
