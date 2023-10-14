idade = 0
soma = 0
qtd = 0

while idade != 1000:
    idade = int(input(f"Digite a idade {qtd+1}: "))
    if idade != 1000:
        soma += idade
        qtd += 1
if qtd == 0:
    print("Não foi digitada uma idade.")
else:
    media = soma / qtd
    print(f"a media das {qtd} idades é: {media}")


