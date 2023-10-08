#receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.

sal_atual = float(input("Digite seu salário atual: "))
percentual = float(input("Percentual de aumento (ex: 25%, 30.5%): ")) / 100

novo_sal = sal_atual * (1 + percentual)


print(f"Seu novo salário é: {novo_sal}. Com um percentual de aumento de: {percentual * 100}%")