sexo = input("Digite M para Masculino ou F para feminino: ")
sexo = sexo.lower()

if sexo == 'm' or sexo == 'f':
    h = float(input("Digite sua altura (ex: 1.75): "))
    if sexo == 'm':
        peso_ideal = (72.7 * h) - 58
        print(f"Seu peso ideal é {peso_ideal}.")
    else:
        peso_ideal2 = (62.1 * h) - 44.7
        print(f"Seu peso ideal é {peso_ideal2}.")

else:
    print("Você digitou M ou F incorretamente.")