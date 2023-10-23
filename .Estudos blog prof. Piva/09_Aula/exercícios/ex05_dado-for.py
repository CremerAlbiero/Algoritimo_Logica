from random import randint
dado = 0
cont1, cont2, cont3, cont4, cont5, cont6 = 0, 0, 0, 0, 0, 0

for i in range(1, 6001):
    dado = randint(1, 6)
    if dado == 1:
        cont1 += 1
    elif dado == 2:
        cont2 += 1
    elif dado == 3:
        cont3 += 1
    elif dado == 4:
        cont4 += 1
    elif dado == 5:
        cont5 += 1
    elif dado == 6:
        cont6 +=1
        
# mostrar a frequencia de cada jogada:
print(f"A frequência em que o dado resultou em 1 foi {cont1} vezes.")
print(f"A frequência em que o dado resultou em 2 foi {cont2} vezes.")
print(f"A frequência em que o dado resultou em 3 foi {cont3} vezes.")
print(f"A frequência em que o dado resultou em 1 foi {cont4} vezes.")
print(f"A frequência em que o dado resultou em 5 foi {cont5} vezes.")
print(f"A frequência em que o dado resultou em 6 foi {cont6} vezes.")

#simular 6000 jogadas de dado de 6 faces. Mostrar a frequência de cada jogada.