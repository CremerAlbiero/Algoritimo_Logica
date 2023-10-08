sal_minimo = float(input("Valor atual do salário mínimo: "))
quilowatt_cons =  float(input("Valor de quilowatt consumido por mês: "))
quilowatt_custo = 0.125 * sal_minimo
a = quilowatt_custo * quilowatt_cons
c = a - (a* 0.15)
print(f"Valor por quilowatt: R$ {quilowatt_custo}")
print(f"Valor a ser pago: R$ {a}")
print(f"Valor a ser pago com 15% de desconto: R$ {c}")

#receba o valor do salário mínimo e a quantidade de quilowatts consumida por uma residência. Calcule e mostre:
#a) O valor, em reais, de cada quilowatt; b) O valor, em reais, a ser pago por essa residência; c) O valor, em reais, a ser pago com desconto de 15%
