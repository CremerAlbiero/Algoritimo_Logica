num = int(input("Digite um número: "))

if num > 0:
    if num % 2 == 0:
        print(f"Número {num} é par")
    else:
        print(f"Número {num} é ímpar.")
else:
    print(f"Erro! o número digitado é menor ou igual a zero.\nDigite um número inteiro maior que zero.")