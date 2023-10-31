# Diferentemente de listas, atribuir a um elemento de um dicionário não requer que a posição exista previamente.

telefones = {"Ana": 17993458329, "Joao": 14886437649, "Pedro": 31697432363}
print(telefones["Pedro"])
# retorna erro, caso a chave nao exista.

# alterar valor da chave:
telefones["Ana"] = 2455632421
print(telefones)

# criar novo elemento. vai para o final da estrutura (novas versões).
telefones["Maria"] = 4345428493
telefones["Felipe"] = 5588742371
print(telefones)


# dict function: converter tupla para dicionário.
tupla = ((1, 'maria'), (2, 'b'))

dicionario = dict(tupla)
print(dicionario)   # {1: 'maria', 2: 'b'}