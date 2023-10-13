idade = int(input("Digite sua idade atual: "))

if idade > 30:
    print("Categoria Sênior.")

elif idade >= 16 and idade <= 30:
    print("Categoria Adulto.")

elif idade >= 11 and idade <= 15:
    print("Categoria Adolescente.")

elif idade >= 8 and idade <= 10:
    print("Categoria Juvenil.")

elif idade >= 5 and idade <= 7:
    print("Categoria Infantil.")

else:
    print("Você não possui idade suficiente para natação.")