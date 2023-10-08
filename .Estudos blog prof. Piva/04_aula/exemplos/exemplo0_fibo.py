a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b


#Se o comando terminar com vírgula, o próximo print escreverá na mesma linha:
a, b = 0,1
while b < 1000:
    print(b, end="")
    a, b = b, a+b