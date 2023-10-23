#criar vetor com 10 elementos numéricos int. Imprimir maior valor e posição na lista.
lista = []

for i in range(1, 11):
    n = int(input(f"Digite o número {i}: "))
    lista.append(n)
maior = max(lista)
print(f"\nO maior valor é {maior}.\nEstá na posição {(lista.index(maior) + 1)} da lista.")

#como o "0" é entendido como a primeira posição, soma +1 para mostrar a posição ao usuário (line 8).