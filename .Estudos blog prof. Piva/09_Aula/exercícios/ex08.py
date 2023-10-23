vetor_a = []
vetor_b = []

for i in range(1, 11):
    numeros = int(input(f"Digite o número {i}: "))
    vetor_a.append(numeros)
    vetor_b.append(numeros)
vetor_b.sort()

print(f"\nVetor a: {vetor_a}")
print(f"Vetor b em ordem crescente de valores: {vetor_b}")