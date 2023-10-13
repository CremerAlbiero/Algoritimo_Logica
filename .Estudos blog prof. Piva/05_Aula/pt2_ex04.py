x = float(input("Digite o valor de X: "))
y = float(input("Digite o valor de Y: "))
z = float(input("Digite o valor de Z: "))

if x + y > z and x + z > y and y + z > x:
    if x == y == z:
        print("triângulo Equilátero.")
    elif x == y or x == z or y == z:
        print("triângulo Isósceles.")
    else:
        print("triângulo Escaleno.")
else:
    print("Essas medidas não formam um triângulo.")