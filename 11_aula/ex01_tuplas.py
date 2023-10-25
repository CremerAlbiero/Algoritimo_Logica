lista = []
for i in range(1, 11):
    numero = int(input(f"Digite o valor {i}: "))
    lista.append(numero)
tupla = tuple(lista)
print(tupla[::-1])

#algoritmo que carregue uma tupla de 10 elementos numéricos inteiros.
# Após a finalização da entrada, o algoritmo deve escrever a mesma tupla, na ordem inversa de entrada.