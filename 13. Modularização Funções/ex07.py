cont = 0
def primos_print(cont, n):
    for i in range(2, n+1):
        if n > 1:
            primo = True
            for i in range(2, n):
                if i % n == 0:
                    primo = False
            if n % i != 0:
                cont += 1
            else:
                primo = False
        else:
            primo =  False
    return cont

n = int(input("Digite um número: "))
total = primos_print(cont, n)
print(total)

