# carregue um dicionario com ome e idade (5 pares)
# depois, mostre todos os nomes que tenham idade maior que a média

pessoas = {}
for i in range(1, 6):
    nome = input(f"Digite o nome {i}: ")
    idade = int(input(f"Digite a idade {i}: "))
    pessoas[nome] = idade
print()

print(pessoas.values()) #values() traz o valor como tuplas.s

total_idades = sum(pessoas.values())
media_idades = total_idades / len(pessoas)     #pega a var da soma e divide pelo comprimento do dict

for nome, idade in pessoas.items():
    if idade > media_idades:
        print(f"{nome} possui idade acima da média.")