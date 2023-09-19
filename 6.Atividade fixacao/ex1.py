import random
numero = int(input("Digite um número que pode ser dividido por 5 e 3 ao: "))

if (numero >= 0):
    if numero % 5 == 0 and numero % 3 == 0:
        print(f"O número {numero} é divisivel por 5 e 3!!!")
        
    else:
        print(f"O número {numero} está incorreto. Bye World.")

