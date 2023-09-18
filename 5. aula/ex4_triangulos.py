x = float(input("valor x: "))
y = float(input("valor y: "))
z = float(input("valor z1: "))

if x + y > z and x + z > y and y + z > x:
    if x == y == z:
        print("Equilátero")
    elif x == y or x == z or y == z:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não é um triângulo")