#receba o valor de um depósito e o valor da taxa de juros, calcule e mostre o valor do rendimento e o valor total depois do rendimento.

deposito = float(input("Digite o valor R$: "))
taxa_juros = float(input("Percentual da taxa(ex: 2%, 3.5%): ")) / 100
meses = int(input("Digite a quantidade de meses: "))


if meses > 1:
    juros_compostos = deposito * (1 + taxa_juros) ** meses
    rendimento = juros_compostos - deposito
    print(f"Seu rendimento foi R${rendimento}.\nMontante final R${juros_compostos}")

else:
    juros_simples = deposito + (deposito * taxa_juros)
    rendimento2 = juros_simples - deposito
    print(f"Seu rendimento foi de R$ {rendimento2}.\nSeu Montante final: R$ {juros_simples}")