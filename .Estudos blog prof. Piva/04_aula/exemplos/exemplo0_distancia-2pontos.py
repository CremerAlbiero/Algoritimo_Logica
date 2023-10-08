x1 = float(input("Entre com x1: "))
y1 = float(input("Entre com y1: "))
x2 = float(input("Entre com x2: "))
y2 = float(input("Entre com y2: "))
dx = x2 - x1
dy = y2 - y1

from math import pow, sqrt

distancia = sqrt(pow(dx,2)+pow(dy,2))
print(distancia)

#pow: retorna a potência de um número inserido. A potência é especificada após a vírgula. 
#Ex pow: pow(2, 4)   resultado = 16.

#sqrt: raiz quadrada