nome = input("Digite seu nome: ")
nome_meio = input("Digite seu nome do meio: ")
sobrenome = input("Digite seu sobrenome: ")

nome_completo = (f"{nome} {nome_meio} {sobrenome}")
print(f"Seu nome é {nome_completo}")

#usando join e lista:
nome_completo = [nome, nome_meio, sobrenome]
nome_completo = " ".join(nome_completo)
print(nome_completo)