n = input("Digite o número do RA: ")

lista = []
for i in n:
    lista.append(int(i))

soma = sum(lista)
print(soma)


multipl = 1
for i in lista:
    num = int(i)
    multipl *= num
print(multipl)