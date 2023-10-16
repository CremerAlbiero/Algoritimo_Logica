number = int(input("Digite um número: "))

if number <= 1:
    print("O número não é primo.")

else:
    primo = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            primo = False
  
    if primo:
        print(f"O Número {number} é primo.")
    else:
        print(f"O Número {number} não é primo")

#praticando a utilização de True / False.