#algoritmo dic 10 elementos onde chave é o sobrenome. 
# e o valor da idade. após isso, algor escreve o sobrenome com a maior idade.

dicionario = {}
for i in range(5):
    sobrenome = input("Digite o sobrenome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    dicionario[sobrenome] = idade

maior_idade = max(dicionario.values())

def mostrar_maior_idade():
    for sobrenome, idade in dicionario.items():
        if idade == maior_idade:
            print(f"{sobrenome} possui a maior idade.")
#não é preciso atribuir o índice, pois ele já encontra a key correspondente ao valor fornecido.

mostrar_maior_idade()