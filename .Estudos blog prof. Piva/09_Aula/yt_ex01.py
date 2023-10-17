cidades_lista = []

while True:
    cidade = input("Digite as cidades que deseja salvar (digite 'sair' quando terminar): ")
    cidade = cidade.lower()
    cidade = cidade.title()
    if cidade == 'Sair':
        break
    else:
        cidades_lista.append(cidade)

if len(cidades_lista) > 1:
    cidades_lista.sort()
print(cidades_lista)