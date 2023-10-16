numero = int(input("Digite um numero inteiro: "))
E = 0

for i in range(1, numero+1):
    if numero > 0:
        E = E + (2 ** i)
print(E)