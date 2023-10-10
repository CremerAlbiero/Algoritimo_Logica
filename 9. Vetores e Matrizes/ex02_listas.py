lista = []
for i in range(5):
    lista.append(int(input(f"Digite o número {i + 1}: ")))
    
maior = max(lista)
posicao = lista.index(maior)
print(lista)

print(f"\nO maior número da lista é: {maior}")
print(posicao)