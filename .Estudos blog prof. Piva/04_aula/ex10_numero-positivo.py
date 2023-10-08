from math import sqrt, pow

numero = 0
while numero <=0:
    numero = int(input("Insira um número maior que zero: "))
    print("Insira um número válido!")

if numero >= 1:
    num_quadrado = pow(numero, 2)
    num_cubo = pow(numero, 3)
    raiz = sqrt(numero)

    print(f"A: {num_quadrado}\nB: {num_cubo}\nC: {raiz}")

#Faça um algoritmo que receba um número positivo e maior que zero, calcule e mostre:
#a) O número digitado ao quadrado
#b) O número digitado ao cubo
#c) A raiz quadrada do número digitado