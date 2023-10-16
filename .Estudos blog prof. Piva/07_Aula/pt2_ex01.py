b = int(input("Digite o valor de b: "))
n = int(input("Digite o valor de n: "))
cont = 0
e = 0

while n and b >= 0:
    cont += 1
    e = (b**n) + e
    if cont == n:
        break
    print(e)