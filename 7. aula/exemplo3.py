soma = 0
qtde = int(input("Digite o valor da quantidade: "))

for i in range(1, qtde+1):
    n = int(input(f"Entre com a {i}. a idade: "))
    soma = soma + n
    media = soma / qtde
print(f"A Media das idadas é {media:5.2f}")