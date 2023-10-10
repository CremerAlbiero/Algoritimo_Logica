from random import randint

lista = [0,0,0,0,0,0,0]

for _ in range(0, 6000):
    lados = randint(1, 6)
    lista[lados] = lista[lados]+1

perc = [0]*7

for i in range(1, 7):
    perc[i] = (lista[i] / 6000) * 100
    print(f"{i} tem um percentual {perc[i]}%")