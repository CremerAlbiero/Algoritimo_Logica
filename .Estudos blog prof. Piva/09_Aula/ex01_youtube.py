cidades_lista = []

while True:
    cidade = input("Digite as cidades que deseja salvar (digite 'sair' quando terminar): ")
    cidade = cidade.lower()
    cidade = cidade.title()
    if cidade == 'Sair':
        break
    else:
        cidades_lista.append(cidade)

if len(cidades_lista) > 0:
    cidades_lista.sort()
    print("As cidades salvas são:\n")
    
    for cidade in cidades_lista:
        
        print(cidade)
else:
    print("Você não digitou nenhuma cidade!")