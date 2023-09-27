from math import sqrt

b = float(input("Digite o valor do cateto b: "))
c = float(input("Digite o valor do cateto c: "))
x = sqrt(b ** 2) + (c ** 2)

print(f"O valor da hipotenusa é {x}")

#sqrt é a raiz quadrada, função importada de "math".