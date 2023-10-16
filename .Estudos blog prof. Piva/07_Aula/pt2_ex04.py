total = 0
cont = 0

while True:
    idade = int(input("Digite a idade: "))
    total += idade
    cont += 1
    if idade == 0:
        cont -= 1
        media = total / cont
        print(f"A média de idade foi de: {media}. Considerando um total de {cont} pessoas.")
        break