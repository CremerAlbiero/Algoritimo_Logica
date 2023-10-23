# algoritmo que leia 20 palavras de no máximo 10 caracteres, e após a leitura, realize um processo qualquer que inverta os caracteres de cada uma das palavras.

palavras = []

for i in range(1, 21):
    word = input(f"Digite a palavra {i} de até 10 caracteres: ")
    if len(word) <=10:
        lista = True
        word = word[::-1]
        palavras.append(word)
    else:
        lista = False
        print("Erro. A palavra não pode ultrapassar 10 caracteres.")
        break
if lista:
    palavras.sort()
    print(f"A lista das palavras, com elas invertidas: {palavras}")
else:
    print("\nRecomece sua lista.")