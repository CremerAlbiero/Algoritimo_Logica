a, b = 1, 1
cont = 0

while cont < 10:
    print(a, end="  ")
    a, b = b, a + b 
    cont += 1