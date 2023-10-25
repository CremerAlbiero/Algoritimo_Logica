lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

conjunto_main = conjunto1.union(conjunto2)

print(f"Conjunto das duas listas: {conjunto_main}")