fatorial = 1
numero = int(input("Digite um número e descubra o fatorial: "))

if numero >= 0:
    for i in range(1, numero + 1):
        fatorial = fatorial * i
    print(f"Fatorial do {numero} é {fatorial}.")

else:
    print("Não há fatorial.")
