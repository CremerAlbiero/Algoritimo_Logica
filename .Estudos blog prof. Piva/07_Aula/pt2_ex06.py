x = int(input("Digite o número (descobrir fatorial): "))
fatorial = 1
cont = 0

while x < 0:
    x = int(input("Digite um número positivo: "))

while cont < x:
    cont += 1
    fatorial *= cont

print(f"Fatorial de {x} é {fatorial}.")