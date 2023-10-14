#Calcular idade de 5 colegas.
soma = 0

for i in range(1, 6):
    idade = int(input(f"Digite sua idade {i}: "))
    soma = soma + idade
    media = soma / 5
print("A media das idades é: ", media)