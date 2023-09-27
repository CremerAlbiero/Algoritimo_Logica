soma = 0
for i in range(1,11 ):
    n = int(input(f"Entre com a {i}. a idade: "))
    soma = soma + n
    media = soma / 10
print(f"A Media das idadas é {media:5.2f}")