b = float(input("Digite a base do triângulo: "))
h = float(input("Digite a altura (h): "))

while b <= 0:
    print("A medida deve ser maior que zero.")
    b = float(input("Digite a base do triângulo: "))

while h <= 0:
    print("A medida deve ser maior que zero.")
    h = float(input("Digite a altura (h): "))

area = (b * h) / 2
print("A área do triângulo é", area)