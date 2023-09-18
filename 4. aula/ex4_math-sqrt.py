from math import pow, sqrt

x1 = int(input("x1:"))
x2 = int(input("x2:"))
y1 = int(input("y1:"))
y2 = int(input("y2:"))

dx = x2-x1
dy = y2-y1

result = sqrt(pow(dx, 2)+pow(dy, 2))

print("A distância entre os pontos é:", result)