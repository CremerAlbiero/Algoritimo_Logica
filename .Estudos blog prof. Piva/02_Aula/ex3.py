#encontrar o maior entre dois números

from random import randint

n1 = randint(0,50)
n2 = randint(0,50)

print(f"Números encontrados: {n1} e {n2}")

if n1 > n2:
    print(f"O número {n1} é maior que {n2}")

elif n1 == n2:
    print(f"Os números são iguais")

else:
    print(f"O número {n2} é maior que {n1}")

#conforme explicado em sala de aula (7), "random" encontra numeros aleatórios em um range(randint) determinado.