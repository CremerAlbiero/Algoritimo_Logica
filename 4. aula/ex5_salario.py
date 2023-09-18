salario = float(input("Salário Prévio: "))
percentual = float(input("Digite o percentual de aumento, (sem o símbolo de porcentagem): "))
aumento = salario + (salario * percentual / 100)
novo = salario * 1.25
print(f"Seu novo salário é: R$ {novo:8.2f}" .replace(".", ","))
print("Você obeteve nov salário: ", novo, "Percentual: ", aumento)