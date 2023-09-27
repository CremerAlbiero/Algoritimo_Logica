while True:
    base = float(input("Entre com a base: "))
    if base > 0:
        break
    print("O valor é invláido, digite um valor maior que 0.")

while True:
    altura = float(input("Entre com a altura: "))
    if altura > 0:
        break
    print("O valor é invláido, digite um valor maior que 0.")

area = (altura + base) / 2
print(f"O valor da área é {area}")