numero = int(input("Digite um número inteiro positivo: "))
fatorial = 1

if numero < 0:
    print("Não existe fatorial de números negativos.")

elif numero == 0:
    print("Fatorial = 1")
else:
    for i in range(1, numero+1):
        fatorial =  fatorial * i
    print(f"Fatorial = {fatorial}")