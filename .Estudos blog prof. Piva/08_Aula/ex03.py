num = input("Digite 9 números: ")

if len(num) == 9:
    int(num)
    print(f"{num[0]}.{num[1:4]}.{num[4:7]},{num[7:9]}")
else:
    print("Deve ser apenas 9 números.")
        