#comando else if (controle de decisão multidirecional)

#exemplo nota:

nota = float(input("Nota: "))
if (nota < 0) or (nota > 1):
    print("Entrada de nota incorreta.")

elif nota >= 0.9:
    print("Nota A")

elif nota >= 0.8:
    print("Nota B")

elif nota >= 0.7:
    print("Nota C")

elif nota >= 0.6:
    print("Nota D")

else:
    print("conceito F")   # < 0.6


#exemplo 2
fruta = input("Entre com a fruta: ")
fruta = fruta.lower()

if fruta == 'banana':
    print("O valor da banana é R$ 5,23")

elif fruta == 'maçã':
    print("O valor da maçã é R$ 12,10")

elif fruta == 'cereja':
    print("O valor da cereja é R$ 58,00")

else:
    print("Só temos as frutas: Banana, Maçã ou Cereja.")