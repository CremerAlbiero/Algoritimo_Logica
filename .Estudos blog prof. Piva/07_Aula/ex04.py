qtde = 0
total = 0

while True:
    numero = int(input("Digite um número par ou ímpar: "))
    if numero != 0:
        if numero % 2 == 0:
            qtde += 1
            total += numero
        else:
            continue
    else:
        break
    
media_pares = total / qtde
print(f"A média dos n pares foi: {media_pares}")

#faça um algoritmo que leia numeros do usuário, mostre a media dos pares (n impedir que ele insira números ímpares). A saída deve ser o numero 0.
