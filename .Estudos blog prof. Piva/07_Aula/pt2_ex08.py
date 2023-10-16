n = int(input("Digite um número primo: "))

while n <= 1:
    n = int(input("Digite um número maior que 1: "))

if n > 1:
    primo = True
    div = 2
    while div < n:
        if n % div == 0:
            primo = False
            break
        div += 1

    if primo:
        print("Numero primo.")
    else:
        print("Falso. Não é um número primo.")