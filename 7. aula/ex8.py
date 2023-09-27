number = int(input("Digite o número: "))
primo = True
n = 0

for i in range(1, number+1):
    if (number % 1) == 0:
        n = n + 1


if n > 2:
    primo = False

if primo:
    print(f"O numero {number} é primo!")

else:
    print(f"O numero {number} não é primo.")





