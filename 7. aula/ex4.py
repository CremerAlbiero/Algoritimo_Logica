soma_pares = 0
qtde_pares = 0

while True:
    entrada = int(input("Digite um número (0 para sair): "))

    if entrada == 0:
        if qtde_apres == 0:
            print("Nenhum número par foi fornecido.")

        else:
            media = soma_pares / qtde_pares
            print(f"A media do snumeros pares fornecidos é: {media}")
            break

            if entrada % 2 == 0:
                soma_pares += entrada
                qtde_pares += 1